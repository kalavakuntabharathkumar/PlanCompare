import { describe,it,expect } from 'vitest';
import { mount } from '@vue/test-utils';
import PlanCard from './PlanCard.vue';
const plan={id:1,name:'Balanced Plus',carrier:'Northstar',annual_premium:2400,deductible:750,copay:25,coverage_percent:85};
describe('PlanCard',()=>{it('renders plan facts',()=>{const w=mount(PlanCard,{props:{plan,selected:false}});expect(w.text()).toContain('Balanced Plus');expect(w.text()).toContain('85%');});it('emits toggle for selected plan action',async()=>{const w=mount(PlanCard,{props:{plan,selected:false}});await w.get('button').trigger('click');expect(w.emitted('toggle')?.[0]).toEqual([1]);});});
