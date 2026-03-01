import streamlit as st

# Main dashboard UI mimicking the screenshot
st.markdown("""
<h1 style="margin-bottom: 0px;">MedSafe AI</h1>
<p style="color: #666; margin-bottom: 2rem; font-weight: 500;">Your Intelligent Healthcare Assistant</p>

<div class="widget-grid">

<!-- Big Green Tool Card: Interaction Checker -->
<a href="interaction_checker" target="_self" class="card-link widget-full">
<div class="card bg-green" style="flex-direction: row; align-items: center;">
<div style="flex: 1;">
<div class="icon-box">💊</div>
<div class="dash-value" style="font-size: 1.8rem;">Interactions</div>
<div class="dash-sub" style="margin-bottom: 12px; margin-top: 4px;">Check drug-to-drug safety</div>
<span style="border: 1px solid #111; padding: 4px 12px; border-radius: 980px; font-size: 0.8rem; font-weight: 600;">Safety</span>
</div>
<div style="flex: 1; text-align: right; font-size: 4rem; opacity: 0.8;">
🛡️
</div>
</div>
</a>

<!-- Small White Tool Card: OCR -->
<a href="prescription_ocr" target="_self" class="card-link">
<div class="card bg-white">
<div class="icon-box" style="background-color: #f7f9fa; box-shadow: none;">📄</div>
<div class="dash-label">Prescription</div>
<div class="dash-sub">AI Scanner</div>
</div>
</a>

<!-- Small Blue Tool Card: Symptom Solver -->
<a href="symptom_solver" target="_self" class="card-link">
<div class="card bg-blue">
<div class="icon-box" style="background-color: #fff; box-shadow: none;">🩺</div>
<div class="dash-label">Symptoms</div>
<div class="dash-sub">AI Guidance</div>
</div>
</a>

<!-- Yellow Info Card -->
<div class="card bg-yellow widget-full" style="flex-direction: row; align-items: center; padding: 16px 24px;">
<div class="icon-box" style="width: 48px; height: 48px; margin-right: 12px; font-size: 1.5rem; background-color: #fff;">💡</div>
<div style="flex: 1;">
<div style="font-weight: 700; font-size: 1.1rem;">Did you know?</div>
<div class="dash-sub">Combining Aspirin & Warfarin can be highly dangerous. Always check!</div>
</div>
</div>

</div>
""", unsafe_allow_html=True)
