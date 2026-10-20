import { describe,it,expect } from 'vitest';
import { setActivePinia,createPinia } from 'pinia';
import { usePlansStore } from './plans';
describe('plans store computed selection',()=>{it('filters and selects plans from the catalogue',()=>{setActivePinia(createPinia());const store=usePlansStore();store.plans=[{id:1,name:'Essential Care',carrier:'Northstar',annual_premium:1800,deductible:1500,copay:35,coverage_percent:80},{id:2,name:'Premium Choice',carrier:'Cedar',annual_premium:3300,deductible:250,copay:15,coverage_percent:90}];store.search='cedar';expect(store.filteredPlans).toHaveLength(1);expect(store.selectedPlans.map(p=>p.id)).toEqual([2]);});});
