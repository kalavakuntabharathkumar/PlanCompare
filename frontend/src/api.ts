import type { Plan, Estimate } from './types';
const API_BASE=import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';
async function request<T>(path:string, init?:RequestInit):Promise<T>{const response=await fetch(`${API_BASE}${path}`,{...init,headers:{'Content-Type':'application/json',...(init?.headers||{})}});if(!response.ok){const body=await response.json().catch(()=>({detail:'Request failed'}));throw new Error(body.detail||'Request failed');}return response.json() as Promise<T>;}
export const api={plans:(search='')=>request<Plan[]>(`/api/plans${search?`?search=${encodeURIComponent(search)}`:''}`),estimate:(payload:{plan_id:number;billed_amount:number;deductible_used:number})=>request<Estimate>('/api/estimate',{method:'POST',body:JSON.stringify(payload)})};
