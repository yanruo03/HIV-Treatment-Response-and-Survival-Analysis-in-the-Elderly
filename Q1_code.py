#%%
pip install statsmodels
#%%
import pandas as pd
import numpy as np
from statsmodels.formula.api import logit
import matplotlib.pyplot as plt
import os

df = pd.read_csv("/Users/pengzhaoying/Desktop/Cleaned_S1_Ageing_Study_Dataset_Cleaned.csv")

# Define Viral Suppression (Y): 1=Suppressed, 0=Not Suppressed
df['suppressed'] = np.where(df['vl_suppressed'] == '<50', 1, 0)
df['years_on_art'] = pd.to_numeric(df['years_on_art'], errors='coerce')
df_clean = df[['suppressed', 'years_on_art']].dropna()

# Fit  Model
model = logit('suppressed ~ years_on_art', data=df_clean).fit(disp=False)

# Extract and Calculate Important Results (OR and CI)
odds_ratio = np.exp(model.params['years_on_art'])
conf_int_95 = np.exp(model.conf_int().loc['years_on_art'])

# Print important calculation results
print("\n[A] Coefficient and P-value:")
print(f"Coefficient (years_on_art): {model.params['years_on_art']:.4f}")
print(f"P-value (years_on_art): {model.pvalues['years_on_art']:.4f}")
print("\n[B] Quantification of Impact (Odds Ratio and 95% CI):")
print(f"Odds Ratio (OR) for one-year increase in ART duration: {odds_ratio:.3f}")
print(f"95% Confidence Interval (CI) for OR: [{conf_int_95[0]:.3f}, {conf_int_95[1]:.3f}]")

# Visualization
X_pred = pd.DataFrame({'years_on_art': np.linspace(df_clean['years_on_art'].min(), df_clean['years_on_art'].max(), 100)})
X_pred['prob_suppressed'] = model.predict(X_pred)
plt.figure(figsize=(8, 6))
# Plot raw data points (jittered)
# Adding some random noise to the Y-axis
plt.scatter(df_clean['years_on_art'],
df_clean['suppressed'] + np.random.uniform(-0.05, 0.05, size=len(df_clean)), alpha=0.2,
 label='Data Points (Jittered)')

# Plot the predicted probability curve
plt.plot(X_pred['years_on_art'], X_pred['prob_suppressed'], color='blue', linewidth=2, label='Predicted Probability Curve')

# Set labels and title
plt.title('Relationship between ART Duration and Probability of Viral Suppression')
plt.xlabel('Duration of ART (Years)')
plt.ylabel('Predicted Probability of Viral Suppression (P(VL < 50))')
plt.yticks([0, 1], ['Not Suppressed (0)', 'Suppressed (1)'])
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
desktop_path = "/Users/pengzhaoying/Desktop/"
plot_filename = "q1_curve.png"
full_path = os.path.join(desktop_path, plot_filename)
plt.savefig(full_path)
plt.show()
#%%

#%%
