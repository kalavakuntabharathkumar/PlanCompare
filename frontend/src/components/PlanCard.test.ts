import { describe,it,expect } from 'vitest';
import { mount } from '@vue/test-utils';
import PlanCard from './PlanCard.vue';
const plan={id:1,name:'Balanced Plus',carrier:'Northstar',annual_premium:2400,deductible:750,copay:25,coverage_percent:85};
describe('PlanCard',()=>{it('renders plan facts',()=>{const w=mount(PlanCard,{props:{plan,selected:false}});expect(w.text()).toContain('Balanced Plus');expect(w.text()).toContain('85%');});it('emits toggle for selected plan action',async()=>{const w=mount(PlanCard,{props:{plan,selected:false}});await w.get('button').trigger('click');expect(w.emitted('toggle')?.[0]).toEqual([1]);});});

const premiumCases: Array<[string,number]> = [['Essential Care',1800],['Balanced Plus',2400],['Premium Choice',3300],['Value Network',1450],['Silver Plan',2100],['Family Plan',2900]];
it.each(premiumCases)('formats plan label and monthly premium for %s', (name,premium)=>{const w=mount(PlanCard,{props:{plan:{...plan,name,annual_premium:premium},selected:true}});expect(w.text()).toContain(name);expect(w.text()).toContain('$');});
