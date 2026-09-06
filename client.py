class MultihopResearchQueryDecomposerClient:
    def decompose_research_query(self, complex_inquiry='Compare geopolitical implications of sodium-ion vs solid-state battery adoption in maritime freight'):
        return {
            'decomposition_id': 'hop_dec_4412',
            'root_inquiry': complex_inquiry,
            'sub_queries_generated': [
                'Sodium-ion energy density and cold-temperature discharge curves',
                'Solid-state battery manufacturing scalability and sulfur supply chain risks',
                'Maritime freight electrification weight constraints and IMO 2030 regulations',
                'Comparative lifecycle cost per kWh in container ship auxiliary power units'
            ],
            'synthesis_dag_waves_count': 2,
            'estimated_sources_needed': 16,
            'query_plan_url': 'https://research.science.genpark.ai/plans/hop_dec_4412.json'
        }
