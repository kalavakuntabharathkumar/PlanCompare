export interface Plan { id:number; name:string; carrier:string; annual_premium:number; deductible:number; copay:number; coverage_percent:number }
export interface Estimate { plan_id:number; billed_amount:number; deductible_applied:number; covered_after_deductible:number; coinsurance_rate:number; copay:number; estimated_member_cost:number; estimated_plan_payment:number }
