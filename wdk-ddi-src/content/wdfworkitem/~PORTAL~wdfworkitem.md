# Declarations in the wdfworkitem header
This header Wdfworkitem contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFWORKITEMCREATE callback function](nc-wdfworkitem-pfn-wdfworkitemcreate.md) | TBD |
| [PFN_WDFWORKITEMFLUSH callback function](nc-wdfworkitem-pfn-wdfworkitemflush.md) | TBD |
| [PFN_WDFWORKITEMGETPARENTOBJECT callback function](nc-wdfworkitem-pfn-wdfworkitemgetparentobject.md) | TBD |
| [PFN_WDFWORKITEMENQUEUE callback function](nc-wdfworkitem-pfn-wdfworkitemenqueue.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfWorkItemCreate function](nf-wdfworkitem-wdfworkitemcreate.md) | The WdfWorkItemCreate method creates a framework work-item object, which can subsequently be added to the system's work-item queue. |
| [WDF_WORKITEM_CONFIG_INIT function](nf-wdfworkitem-wdf-workitem-config-init.md) | The WDF_WORKITEM_CONFIG_INIT function initializes a driver's WDF_WORKITEM_CONFIG structure. |
| [WdfWorkItemGetParentObject function](nf-wdfworkitem-wdfworkitemgetparentobject.md) | The WdfWorkItemGetParentObject method returns the framework object that a specified work item is associated with. |
| [WdfWorkItemFlush function](nf-wdfworkitem-wdfworkitemflush.md) | The WdfWorkItemFlush method returns after a specified work item has been serviced. |
| [WdfWorkItemEnqueue function](nf-wdfworkitem-wdfworkitemenqueue.md) | The WdfWorkItemEnqueue method adds a specified framework work-item object to the system's work-item queue. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_WORKITEM_CONFIG structure](ns-wdfworkitem--wdf-workitem-config.md) | The WDF_WORKITEM_CONFIG structure contains information that is associated with a work item. |

This header is used in these topics:

- [wdf](..content/_wdf)
