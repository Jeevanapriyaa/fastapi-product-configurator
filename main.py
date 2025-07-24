from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Data models
class ProductTemplate(BaseModel):
    id: int
    name: str

class OptionCategory(BaseModel):
    id: int
    name: str
    product_template_id: int

class Choice(BaseModel):
    id: int
    name: str
    category_id: int

class CompatibilityRule(BaseModel):
    id: int
    compatible_choices: List[int]  # list of choice IDs that are compatible together

class Selection(BaseModel):
    selected_choices: List[int]

# In-memory storage
product_templates: Dict[int, ProductTemplate] = {}
categories: Dict[int, OptionCategory] = {}
choices: Dict[int, Choice] = {}
rules: List[CompatibilityRule] = []

# API Endpoints

@app.post("/product-templates/")
def create_product_template(template: ProductTemplate):
    if template.id in product_templates:
        raise HTTPException(status_code=400, detail="Template ID already exists")
    product_templates[template.id] = template
    return template

@app.post("/option-categories/")
def create_option_category(category: OptionCategory):
    if category.id in categories:
        raise HTTPException(status_code=400, detail="Category ID already exists")
    if category.product_template_id not in product_templates:
        raise HTTPException(status_code=404, detail="Product template not found")
    categories[category.id] = category
    return category

@app.post("/choices/")
def create_choice(choice: Choice):
    if choice.id in choices:
        raise HTTPException(status_code=400, detail="Choice ID already exists")
    if choice.category_id not in categories:
        raise HTTPException(status_code=404, detail="Option category not found")
    choices[choice.id] = choice
    return choice

@app.post("/compatibility-rules/")
def create_compatibility_rule(rule: CompatibilityRule):
    rules.append(rule)
    return rule

@app.post("/validate-selection/")
def validate_selection(selection: Selection):
    selected_set = set(selection.selected_choices)
    for rule in rules:
        rule_set = set(rule.compatible_choices)
        if selected_set.issubset(rule_set):
            return {"valid": True, "message": "Selection is compatible"}
    return {"valid": False, "message": "Selection is incompatible"}

# Sample Test Endpoint (Optional)
@app.get("/")
def root():
    return {"message": "Product Configuration API is working"}
