# Ucmmanager.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucmmanager.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCM_CONNECTOR_CONFIG_INIT function](nf-ucmmanager-ucm-connector-config-init.md) | Initializes a UCM_CONNECTOR_CONFIG structure. |
| [UCM_CONNECTOR_PD_CONFIG_INIT function](nf-ucmmanager-ucm-connector-pd-config-init.md) | Initializes a UCM_CONNECTOR_PD_CONFIG structure. |
| [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS_INIT function](nf-ucmmanager-ucm-connector-pd-conn-state-changed-params-init.md) | Initializes a UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure. |
| [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS_INIT function](nf-ucmmanager-ucm-connector-typec-attach-params-init.md) | Initializes a UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure. |
| [UCM_MANAGER_CONFIG_INIT function](nf-ucmmanager-ucm-manager-config-init.md) | Initializes a UCM_MANAGER_CONFIG structure. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_UCM_CONNECTOR_SET_DATA_ROLE callback](nc-ucmmanager-evt-ucm-connector-set-data-role.md) | The client driver's implementation of the EVT_UCM_CONNECTOR_SET_DATA_ROLE event callback function that swaps the data role of the connector to the specified role when attached to a partner connector. |
| [EVT_UCM_CONNECTOR_SET_POWER_ROLE callback](nc-ucmmanager-evt-ucm-connector-set-power-role.md) | The client driver's implementation of the EVT_UCM_CONNECTOR_SET_POWER_ROLE event callback function that sets the power role of the connector to the specified role when attached to a partner connector. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [UCM_CONNECTOR_CONFIG structure](ns-ucmmanager--ucm-connector-config.md) | Describes the configuration options for a Type-C connector object. An initialized UCM_MANAGER_CONFIG structure is an input parameter value to UcmInitializeDevice. |
| [UCM_CONNECTOR_PD_CONFIG structure](ns-ucmmanager--ucm-connector-pd-config.md) | Describes the Power Delivery 2.0 capabilities of the connector. |
| [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure](ns-ucmmanager--ucm-connector-pd-conn-state-changed-params.md) | Describes the parameters for PD connection changed event. |
| [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure](ns-ucmmanager--ucm-connector-typec-attach-params.md) | Describes the partner that is currently attached to the connector. |
| [UCM_CONNECTOR_TYPEC_CONFIG structure](ns-ucmmanager--ucm-connector-typec-config.md) | Describes the configuration options for a Type-C connector. |
| [UCM_MANAGER_CONFIG structure](ns-ucmmanager--ucm-manager-config.md) | Describes the configuration options for the UCM Manager. An initialized UCM_MANAGER_CONFIG structure is an input parameter value to UcmInitializeDevice. |
