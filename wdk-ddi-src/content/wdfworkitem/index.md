---
UID: NA:wdfworkitem
---

# Wdfworkitem.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfworkitem.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFWORKITEMCREATE function](nc-wdfworkitem-pfn_wdfworkitemcreate.md) | The WdfWorkItemCreate method creates a framework work-item object, which can subsequently be added to the system's work-item queue. |
| [PFN_WDFWORKITEMENQUEUE function](nc-wdfworkitem-pfn_wdfworkitemenqueue.md) | The WdfWorkItemEnqueue method adds a specified framework work-item object to the system's work-item queue. |
| [PFN_WDFWORKITEMFLUSH function](nc-wdfworkitem-pfn_wdfworkitemflush.md) | The WdfWorkItemFlush method returns after a specified work item has been serviced. |
| [PFN_WDFWORKITEMGETPARENTOBJECT function](nc-wdfworkitem-pfn_wdfworkitemgetparentobject.md) | The WdfWorkItemGetParentObject method returns the framework object that a specified work item is associated with. |
| [WDF_WORKITEM_CONFIG_INIT function](nf-wdfworkitem-wdf_workitem_config_init.md) | The WDF_WORKITEM_CONFIG_INIT function initializes a driver's WDF_WORKITEM_CONFIG structure. |
| [WdfWorkItemCreate function](nf-wdfworkitem-wdfworkitemcreate.md) | The WdfWorkItemCreate method creates a framework work-item object, which can subsequently be added to the system's work-item queue. |
| [WdfWorkItemEnqueue function](nf-wdfworkitem-wdfworkitemenqueue.md) | The WdfWorkItemEnqueue method adds a specified framework work-item object to the system's work-item queue. |
| [WdfWorkItemFlush function](nf-wdfworkitem-wdfworkitemflush.md) | The WdfWorkItemFlush method returns after a specified work item has been serviced. |
| [WdfWorkItemGetParentObject function](nf-wdfworkitem-wdfworkitemgetparentobject.md) | The WdfWorkItemGetParentObject method returns the framework object that a specified work item is associated with. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_WORKITEM_CONFIG structure](ns-wdfworkitem-_wdf_workitem_config.md) | The WDF_WORKITEM_CONFIG structure contains information that is associated with a work item. |
