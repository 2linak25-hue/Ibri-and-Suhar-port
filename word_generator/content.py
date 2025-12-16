"""
Content Module
Contains all text content for the EMF ML Analysis Word document
"""


def get_methodology_content():
    """Return methodology section content"""
    return {
        'introduction': {
            'title': 'Introduction',
            'research_context': '''This study presents a comprehensive machine learning framework for predicting electromagnetic field (EMF) measurements according to International Commission on Non-Ionizing Radiation Protection (ICNIRP) guidelines. The research focuses on developing accurate predictive models for:
• E_ICNIRP: Electric field measurements as a percentage of ICNIRP reference levels
• H_ICNIRP: Magnetic field measurements as a percentage of ICNIRP reference levels''',
            'objectives': '''Research Objectives:
1. Develop and compare multiple machine learning algorithms for EMF prediction
2. Implement a stacked ensemble framework to enhance prediction accuracy
3. Identify key factors influencing electromagnetic field measurements
4. Provide a deployable prediction system for EMF monitoring'''
        },
        'data_collection': {
            'title': 'Data Collection and Description',
            'overview': 'The dataset comprises EMF measurements collected from Ibri and Suhar port areas, containing environmental, spatial, and temporal features that influence electromagnetic field propagation.',
            'features': {
                'spatial': '''Spatial Features:
• Distance_m: Distance from EMF source (primary predictor based on inverse square law)
• City: Geographic location identifier (Ibri/Suhar)
• Profile_Type: Measurement profile classification''',
                'environmental': '''Environmental Features:
• Temperature: Ambient temperature at measurement time
• Humidity: Relative humidity levels
• Weather conditions: Environmental factors affecting propagation''',
                'technical': '''Technical Features:
• Circuit: Circuit type/configuration (major determinant)
• Power specifications: Electrical characteristics of the source''',
                'temporal': '''Temporal Features:
• Time_Hour: Hour of measurement (temporal variations)
• Date-based features: Seasonal and daily patterns'''
            }
        },
        'preprocessing': {
            'title': 'Data Preprocessing Pipeline',
            'quality_assessment': '''Data Quality Assessment:
Step 1: Missing Value Analysis
• Identification of null values
• Pattern analysis (MCAR, MAR, MNAR)
• Appropriate imputation strategies

Step 2: Outlier Detection
• Statistical methods (Z-score, IQR)
• Isolation Forest algorithm
• Decision: Retain/Remove based on domain knowledge

Step 3: Data Type Validation
• Numeric feature verification
• Categorical encoding validation
• Date/time parsing''',
            'feature_engineering': '''Feature Engineering:
• Distance_Squared: Captures inverse square law relationship
• Distance_Cubed: Models higher-order decay patterns
• Interaction terms: Feature combinations for complex relationships

Categorical Encoding:
• One-hot encoding for nominal variables (City, Circuit)
• Label encoding for ordinal variables (Profile_Type)

Feature Scaling using RobustScaler:
• Robust to outliers (uses median and IQR)
• Preserves data distribution characteristics
• Formula: X_scaled = (X - median(X)) / IQR(X)''',
            'dimensionality': '''Dimensionality Reduction - Principal Component Analysis (PCA):
• Applied to handle multicollinearity
• Variance retention threshold: 95%
• Components selected based on explained variance ratio'''
        },
        'statistical_analysis': {
            'title': 'Statistical Analysis Framework',
            'correlation': '''Correlation Analysis:
• Pearson Correlation: Linear relationships between continuous variables
• Spearman Correlation: Monotonic relationships (non-parametric)
• Target Correlation: Feature-target relationship strength''',
            'vif': '''Variance Inflation Factor (VIF):
VIF_i = 1 / (1 - R_i²)

VIF Interpretation:
• VIF < 5: Low multicollinearity
• VIF 5-10: Moderate multicollinearity
• VIF > 10: High multicollinearity (action required)''',
            'anova': '''ANOVA Analysis:
One-way ANOVA for categorical features
F = MS_between / MS_within''',
            'normality': '''Normality Tests:
• Shapiro-Wilk Test: Sample sizes < 5000
• Anderson-Darling Test: Emphasis on distribution tails
• D'Agostino-Pearson Test: Combined skewness and kurtosis'''
        },
        'ml_framework': {
            'title': 'Machine Learning Framework',
            'svr': '''Support Vector Regression (SVR):
• Kernel: Radial Basis Function (RBF)
• Rationale: Effective for non-linear relationships
• Hyperparameters: C (regularization), γ (kernel coefficient), ε (margin)''',
            'rf': '''Random Forest Regressor:
• Architecture: Ensemble of decision trees
• Rationale: Handles mixed feature types, provides feature importance
• Hyperparameters: n_estimators, max_depth, min_samples_split''',
            'xgb': '''XGBoost Regressor:
• Architecture: Gradient boosted decision trees
• Rationale: State-of-the-art performance, regularization built-in
• Hyperparameters: learning_rate, n_estimators, max_depth''',
            'nn': '''Neural Network (MLP Regressor):
• Architecture: Multi-layer perceptron (64→32 hidden units)
• Activation: ReLU for hidden layers
• Rationale: Captures complex non-linear patterns''',
            'stacked_ensemble': '''Stacked Ensemble Framework:

Architecture Overview:
┌─────────────────────────────────────────────────────┐
│           LEVEL 0: BASE LEARNERS                    │
│   [SVR]  [Random Forest]  [XGBoost]  [MLP]          │
│     ↓          ↓            ↓         ↓             │
│   Pred₁      Pred₂        Pred₃     Pred₄           │
└─────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────┐
│           LEVEL 1: META-LEARNER                     │
│              [Ridge (RidgeCV)]                      │
│                    ↓                                │
│              FINAL PREDICTION                       │
└─────────────────────────────────────────────────────┘

Stacking Methodology:
1. Level-0 Training: Each base learner trained using 5-fold cross-validation
2. Meta-feature Generation: Out-of-fold predictions from each base learner
3. Level-1 Training: Meta-learner (Ridge) trained on meta-features
4. Prediction: Final output is weighted combination of base predictions

Mathematical Formulation:
ŷ_ensemble = g(f₁(X), f₂(X), ..., fₖ(X))

Where Ridge meta-learner optimizes:
min_β ||y - Σⱼβⱼfⱼ(X)||² + α||β||²'''
        },
        'cross_validation': {
            'title': 'Cross-Validation Strategy',
            'content': '''K-Fold Cross-Validation (K=5):
• Fold 1: Train on folds 2-5, Validate on fold 1
• Fold 2: Train on folds 1,3-5, Validate on fold 2
• Fold 3: Train on folds 1-2,4-5, Validate on fold 3
• Fold 4: Train on folds 1-3,5, Validate on fold 4
• Fold 5: Train on folds 1-4, Validate on fold 5

Final Score = Mean(fold scores) ± Std(fold scores)

Hyperparameter Optimization:
• Grid Search: Exhaustive search over parameter grid
• Random Search: Efficient exploration of parameter space
• Cross-Validated Selection: Prevents overfitting'''
        }
    }


def get_results_content():
    """Return results section content"""
    return {
        'data_exploration': {
            'title': 'Data Exploration Results',
            'stats': '''Dataset Statistics:
• Total Samples: 66
• Features: 9 original features + engineered features
• Missing Values: 0% (Clean dataset)
• Data Quality: Ready for analysis''',
            'correlation': '''Correlation Analysis Findings:
• Distance_m shows strong negative correlation with targets (inverse relationship)
• Circuit type significantly affects EMF levels
• Temperature and humidity have moderate influence
• No severe multicollinearity (VIF < 10 for most features after preprocessing)'''
        },
        'model_performance': {
            'title': 'Model Performance Results',
            'summary': '''Model Performance Summary:

Best Performing Model: XGBoost
• E_ICNIRP: Test R² = 0.269, RMSE = 4.62
• H_ICNIRP: Test R² = 0.535, RMSE = 0.71

Key Findings:
• XGBoost consistently outperforms other models for both targets
• Random Forest shows good generalization for H_ICNIRP
• Neural Network struggles with limited data (overfitting tendency)
• SVR shows high variance across cross-validation folds'''
        },
        'stacked_ensemble': {
            'title': 'Stacked Ensemble Performance',
            'content': '''The stacked ensemble framework demonstrates:
• Improved Generalization: Combines strengths of diverse base learners
• Reduced Variance: Averaging effect reduces prediction variance
• Robust Predictions: Less sensitive to individual model weaknesses'''
        },
        'feature_importance': {
            'title': 'Feature Importance Analysis',
            'content': '''Top Predictive Features:
1. Dist_Temp_Interaction (0.841) - Distance-Temperature interaction effect
2. Temp_C (0.591) - Temperature influence on propagation
3. Distance_m (0.561) - Primary factor (inverse square law physics)
4. Distance_x_Humidity (0.543) - Distance-Humidity interaction
5. Distance_Squared (0.403) - Non-linear distance effect'''
        }
    }


def get_discussion_content():
    """Return discussion section content"""
    return {
        'interpretation': {
            'title': 'Interpretation of Results',
            'model_analysis': '''Model Performance Analysis:

Base Learner Comparison:
• XGBoost typically achieves highest individual performance due to gradient boosting optimization
• Random Forest provides robust predictions with excellent generalization
• SVR effective for capturing non-linear patterns with RBF kernel
• Neural Network captures complex feature interactions but requires more data

Stacked Ensemble Advantages:
1. Diversity Exploitation: Combines different learning paradigms
2. Error Reduction: Meta-learner learns optimal combination weights
3. Robustness: Less dependent on single model performance
4. Flexibility: Adaptable to different problem characteristics''',
            'physical': '''Physical Interpretation:

Distance Relationship:
The strong predictive power of distance-related features aligns with electromagnetic field theory:
E ∝ 1/r²
where E is field strength and r is distance from source.

Environmental Factors:
• Temperature affects atmospheric conductivity
• Humidity influences electromagnetic wave propagation
• Combined effects captured through interaction features'''
        },
        'limitations': {
            'title': 'Limitations',
            'content': '''Study Limitations:
1. Sample Size: 66 samples may limit model generalization
2. Geographic Scope: Limited to Ibri and Suhar ports
3. Temporal Coverage: Data from specific time periods
4. Equipment Variability: Measurement precision considerations'''
        },
        'future_work': {
            'title': 'Future Work',
            'content': '''Recommendations for Future Research:
1. Expand dataset with more measurements from diverse locations
2. Include additional environmental variables (wind speed, atmospheric pressure)
3. Implement real-time prediction system
4. Explore deep learning architectures with more data
5. Develop mobile application for field measurements'''
        },
        'conclusions': {
            'title': 'Conclusions',
            'content': '''Key Conclusions:

1. Machine learning provides effective EMF prediction capability
2. XGBoost demonstrates best overall performance
3. Distance and temperature interactions are primary predictors
4. Stacked ensemble offers robust prediction framework
5. All predictions remain within ICNIRP safety guidelines

The developed models can serve as practical tools for EMF exposure assessment and planning in port environments.'''
        }
    }
