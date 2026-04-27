## Car Racing con Gymnasium y PPO

En el folder `corridas` se encuentra un subfolder por cada experimento realizado, donde se documenta en detalle la configuración utilizada en cada corrida, la motivación detrás de ese cambio respecto de la corrida anterior y los resultados obtenidos tanto a nivel cuantitativo como cualitativo; además, en el folder `videos` de cada corrida pueden verse los episodios grabados para analizar visualmente el comportamiento del agente.

Particularmente interesantes son [`01_baseline`](corridas/01_baseline), donde se describe en detalle la configuración utilizada, y [`10_observation_resize`](corridas/10_observation_resize), donde se puede ver el detalle de la los mejores resultados.

### Mejor corrida:

La mejor corrida obtenida fue [`10_observation_resize`](corridas/10_observation_resize), ya que combinó un rendimiento cuantitativo alto con un comportamiento cualitativo claramente superior al de las corridas anteriores: alcanzó rewards elevados de forma sostenida, mostró una conducción más estable y logró completar correctamente una vuelta, mientras que en otras configuraciones observamos con mayor frecuencia oscilaciones, salidas de pista o recuperación en sentido incorrecto. Además, las corridas multiseed basadas en esta configuración mostraron que el cambio de observación mediante resize fue una mejora relevante y no solo un resultado aislado. En el video se puede ver que el agente completa una vuelta correctamente: [`video`](corridas/10_observation_resize/experiments/carracing_ppo/run_20260424_113851_seed0/videos/best_model_eval-step-0-to-step-2000.mp4)

Se puede ver el detalle de los resultados de esa corrida en la notebook eval y en el video.

![](corridas/10_observation_resize/experiments/carracing_ppo/run_20260424_113851_seed0/convergencia_reward_vs_episodios.png)

![](corridas/10_observation_resize/experiments/carracing_ppo/run_20260424_113851_seed0/evaluacion_periodica_reward_medio_vs_timesteps.png)

### Código más relevante:

```python
def main() -> None:
    cfg = get_config()
    set_global_seeds(cfg.seed)
    paths = make_run_dirs(cfg)
    export_config(cfg, paths)

    print("=" * 80)
    print("CarRacing-v3 PPO baseline")
    print(f"Run dir:          {paths['base']}")
    print(f"Seed:             {cfg.seed}")
    print(f"Total timesteps:  {cfg.total_timesteps}")
    print(f"Parallel envs:    {cfg.n_envs}")
    print(f"Eval every:       {cfg.eval_freq_steps} env steps")
    print(f"Checkpoint every: {cfg.checkpoint_freq_steps} env steps")
    print("=" * 80)

    train_env = make_train_vec_env(cfg, paths)
    eval_env = make_eval_vec_env(cfg, paths)

    model = build_model(cfg, train_env, paths)
    callbacks = build_callbacks(cfg, eval_env, paths)

    try:
        model.learn(
            total_timesteps=cfg.total_timesteps,
            callback=callbacks,
            progress_bar=True,
            tb_log_name="ppo_carracing",
            reset_num_timesteps=True,
        )

        final_model_path = paths["base"] / "final_model.zip"
        model.save(str(final_model_path))
        print(f"Saved final model to: {final_model_path}")
        print(f"Best model path:      {paths['best_model']}")
        print(f"TensorBoard log dir:  {paths['tb']}")

    finally:
        train_env.close()
        eval_env.close()
```