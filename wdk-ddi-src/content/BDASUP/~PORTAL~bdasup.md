# Declarations in the bdasup header
This header Bdasup contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [BdaInitFilter function](nf-bdasup-bdainitfilter.md) | The BdaInitFilter function initializes the BDA filter context associated with a filter instance. |
| [BdaGetChangeState function](nf-bdasup-bdagetchangestate.md) | The BdaGetChangeState function returns the current change state of BDA topology. |
| [BdaCheckChanges function](nf-bdasup-bdacheckchanges.md) | The BdaCheckChanges function verifies a new set of BDA topology changes before they are committed. |
| [BdaCreateFilterFactoryEx function](nf-bdasup-bdacreatefilterfactoryex.md) | The BdaCreateFilterFactoryEx function adds the specified filter descriptor as a filter factory to the specified device and associates the filter factory with the specified BDA template topology. |
| [BdaMethodCreatePin function](nf-bdasup-bdamethodcreatepin.md) | The BdaMethodCreatePin function creates a pin factory. |
| [BdaStartChanges function](nf-bdasup-bdastartchanges.md) | The BdaStartChanges function initiates the setting of new BDA topology changes. |
| [BdaPropertyNodeProperties function](nf-bdasup-bdapropertynodeproperties.md) | The BdaPropertyNodeProperties function retrieves a list of properties that a node supports. |
| [BdaCommitChanges function](nf-bdasup-bdacommitchanges.md) | The BdaCommitChanges function commits the changes to BDA topology that have occurred since the last call to the BdaStartChanges function. |
| [BdaUninitFilter function](nf-bdasup-bdauninitfilter.md) | The BdaUninitFilter function removes the BDA filter context from the associated filter instance. |
| [BdaPropertyNodeDescriptors function](nf-bdasup-bdapropertynodedescriptors.md) | The BdaPropertyNodeDescriptors function retrieves a list of nodes in a template topology. |
| [BdaCreateFilterFactory function](nf-bdasup-bdacreatefilterfactory.md) | The BdaCreateFilterFactory function adds the specified filter descriptor as a filter factory to the specified device and associates the filter factory with the specified BDA template topology. |
| [BdaPropertyGetPinControl function](nf-bdasup-bdapropertygetpincontrol.md) | The BdaPropertyGetPinControl function retrieves either the identifier or type of a pin. |
| [BdaCreateTopology function](nf-bdasup-bdacreatetopology.md) | The BdaCreateTopology function creates the topology between two pins. |
| [BdaPropertyGetControllingPinId function](nf-bdasup-bdapropertygetcontrollingpinid.md) | The BdaPropertyGetControllingPinId function retrieves the identifier of a pin on which to control the properties, methods, and events of a specific node. |
| [BdaPropertyNodeMethods function](nf-bdasup-bdapropertynodemethods.md) | The BdaPropertyNodeMethods function retrieves a list of methods that a node supports. |
| [BdaPropertyNodeTypes function](nf-bdasup-bdapropertynodetypes.md) | The BdaPropertyNodeTypes function retrieves a list of node types in a template topology. |
| [BdaPropertyPinTypes function](nf-bdasup-bdapropertypintypes.md) | The BdaPropertyPinTypes function retrieves a list of pin types in a template topology. |
| [BdaDeletePin function](nf-bdasup-bdadeletepin.md) | The BdaDeletePin function deletes a pin from the specified filter. |
| [BdaPropertyNodeEvents function](nf-bdasup-bdapropertynodeevents.md) | The BdaPropertyNodeEvents function retrieves a list of events that a node supports. |
| [BdaValidateNodeProperty function](nf-bdasup-bdavalidatenodeproperty.md) | The BdaValidateNodeProperty function validates that a node property request is associated with a specific pin. |
| [BdaMethodCreateTopology function](nf-bdasup-bdamethodcreatetopology.md) | The BdaMethodCreateTopology function creates a template topology between two pins of a filter. |
| [BdaPropertyTemplateConnections function](nf-bdasup-bdapropertytemplateconnections.md) | The BdaPropertyTemplateConnections function retrieves a list of connections that describe how pin types and node types are connected in a template topology. |
| [BdaCreatePin function](nf-bdasup-bdacreatepin.md) | The BdaCreatePin function creates a new pin in the specified filter. |
| [BdaMethodDeletePin function](nf-bdasup-bdamethoddeletepin.md) | The BdaMethodDeletePin function deletes a pin factory. |
| [BdaFilterFactoryUpdateCacheData function](nf-bdasup-bdafilterfactoryupdatecachedata.md) | The BdaFilterFactoryUpdateCacheData function updates the pin data cache for an instance of a filter. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BDA_PIN_PAIRING structure](ns-bdasup--bda-pin-pairing.md) | The BDA_PIN_PAIRING structure describes the topology between a pair of input and output pins. |
| [KSM_PIN structure](ns-bdasup--ksm-pin.md) | The KSM_PIN structure describes a method request to create or delete a pin factory for a filter. |
| [KSM_PIN_PAIR structure](ns-bdasup--ksm-pin-pair.md) | The KSM_PIN_PAIR structure describes a method request to retrieve the pin pairing structure (BDA_PIN_PAIRING) between a pair of input and output pins. |
| [BDA_FILTER_TEMPLATE structure](ns-bdasup--bda-filter-template.md) | The BDA_FILTER_TEMPLATE structure describes the template topology for a BDA filter. |

This header is used in these topics:

- [stream](..content/_stream)
