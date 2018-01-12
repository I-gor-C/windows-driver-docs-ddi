---
UID: NA:wdfresource
---

# Wdfresource.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfresource.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFCMRESOURCELISTAPPENDDESCRIPTOR function](nc-wdfresource-pfn_wdfcmresourcelistappenddescriptor.md) | The WdfCmResourceListAppendDescriptor method adds a resource descriptor to the end of a specified resource list. |
| [PFN_WDFCMRESOURCELISTGETCOUNT function](nc-wdfresource-pfn_wdfcmresourcelistgetcount.md) | The WdfCmResourceListGetCount method returns the number of resource descriptors that are contained in a specified resource list. |
| [PFN_WDFCMRESOURCELISTGETDESCRIPTOR function](nc-wdfresource-pfn_wdfcmresourcelistgetdescriptor.md) | The WdfCmResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a specified resource list. |
| [PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR function](nc-wdfresource-pfn_wdfcmresourcelistinsertdescriptor.md) | The WdfCmResourceListInsertDescriptor method inserts a resource descriptor into a specified resource list. |
| [PFN_WDFCMRESOURCELISTREMOVE function](nc-wdfresource-pfn_wdfcmresourcelistremove.md) | The WdfCmResourceListRemove method removes a resource descriptor from a specified resource list. |
| [PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR function](nc-wdfresource-pfn_wdfcmresourcelistremovebydescriptor.md) | The WdfCmResourceListRemoveByDescriptor method removes a specified resource descriptor from a specified resource list. |
| [PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR function](nc-wdfresource-pfn_wdfioresourcelistappenddescriptor.md) | The WdfIoResourceListAppendDescriptor method adds a resource descriptor to the end of a resource requirements list's logical configuration. |
| [PFN_WDFIORESOURCELISTCREATE function](nc-wdfresource-pfn_wdfioresourcelistcreate.md) | The WdfIoResourceListCreate method creates an empty logical configuration, which can be populated and added to a resource requirements list. |
| [PFN_WDFIORESOURCELISTGETCOUNT function](nc-wdfresource-pfn_wdfioresourcelistgetcount.md) | The WdfIoResourceListGetCount method returns the number of resource descriptors that are contained in a resource requirements list's logical configuration. |
| [PFN_WDFIORESOURCELISTGETDESCRIPTOR function](nc-wdfresource-pfn_wdfioresourcelistgetdescriptor.md) | The WdfIoResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a resource requirements list's logical configuration. |
| [PFN_WDFIORESOURCELISTINSERTDESCRIPTOR function](nc-wdfresource-pfn_wdfioresourcelistinsertdescriptor.md) | The WdfIoResourceListInsertDescriptor method inserts a resource descriptor into a resource requirements list's logical configuration. |
| [PFN_WDFIORESOURCELISTREMOVE function](nc-wdfresource-pfn_wdfioresourcelistremove.md) | The WdfIoResourceListRemove method removes a resource descriptor from a resource requirements list's logical configuration. |
| [PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR function](nc-wdfresource-pfn_wdfioresourcelistremovebydescriptor.md) | The WdfIoResourceListRemoveByDescriptor method removes a resource descriptor from a resource requirement list's logical configuration. |
| [PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR function](nc-wdfresource-pfn_wdfioresourcelistupdatedescriptor.md) | The WdfIoResourceListUpdateDescriptor method updates a resource descriptor in a resource requirements list's logical configuration. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST function](nc-wdfresource-pfn_wdfioresourcerequirementslistappendioreslist.md) | The WdfIoResourceRequirementsListAppendIoResList method adds a logical configuration to the end of a resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT function](nc-wdfresource-pfn_wdfioresourcerequirementslistgetcount.md) | The WdfIoResourceRequirementsListGetCount method returns the number of logical configurations that are contained in a resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST function](nc-wdfresource-pfn_wdfioresourcerequirementslistgetioreslist.md) | The WdfIoResourceRequirementsListGetIoResList method returns a handle to the framework resource-range-list object that represents a specified logical configuration in a specified resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST function](nc-wdfresource-pfn_wdfioresourcerequirementslistinsertioreslist.md) | The WdfIoResourceRequirementsListInsertIoResList method inserts a logical configuration into a resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVE function](nc-wdfresource-pfn_wdfioresourcerequirementslistremove.md) | The WdfIoResourceRequirementsListRemove method removes a logical configuration from a resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST function](nc-wdfresource-pfn_wdfioresourcerequirementslistremovebyioreslist.md) | The WdfIoResourceRequirementsListRemoveByIoResList method removes a logical configuration from a resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE function](nc-wdfresource-pfn_wdfioresourcerequirementslistsetinterfacetype.md) | The WdfIoResourceRequirementsListSetInterfaceType method assigns a bus type to a resource requirements list. |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER function](nc-wdfresource-pfn_wdfioresourcerequirementslistsetslotnumber.md) | The WdfIoResourceRequirementsListSetSlotNumber method assigns a slot number to a resource requirements list. |
| [WdfCmResourceListAppendDescriptor function](nf-wdfresource-wdfcmresourcelistappenddescriptor.md) | The WdfCmResourceListAppendDescriptor method adds a resource descriptor to the end of a specified resource list. |
| [WdfCmResourceListGetCount function](nf-wdfresource-wdfcmresourcelistgetcount.md) | The WdfCmResourceListGetCount method returns the number of resource descriptors that are contained in a specified resource list. |
| [WdfCmResourceListGetDescriptor function](nf-wdfresource-wdfcmresourcelistgetdescriptor.md) | The WdfCmResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a specified resource list. |
| [WdfCmResourceListInsertDescriptor function](nf-wdfresource-wdfcmresourcelistinsertdescriptor.md) | The WdfCmResourceListInsertDescriptor method inserts a resource descriptor into a specified resource list. |
| [WdfCmResourceListRemove function](nf-wdfresource-wdfcmresourcelistremove.md) | The WdfCmResourceListRemove method removes a resource descriptor from a specified resource list. |
| [WdfCmResourceListRemoveByDescriptor function](nf-wdfresource-wdfcmresourcelistremovebydescriptor.md) | The WdfCmResourceListRemoveByDescriptor method removes a specified resource descriptor from a specified resource list. |
| [WdfIoResourceListAppendDescriptor function](nf-wdfresource-wdfioresourcelistappenddescriptor.md) | The WdfIoResourceListAppendDescriptor method adds a resource descriptor to the end of a resource requirements list's logical configuration. |
| [WdfIoResourceListCreate function](nf-wdfresource-wdfioresourcelistcreate.md) | The WdfIoResourceListCreate method creates an empty logical configuration, which can be populated and added to a resource requirements list. |
| [WdfIoResourceListGetCount function](nf-wdfresource-wdfioresourcelistgetcount.md) | The WdfIoResourceListGetCount method returns the number of resource descriptors that are contained in a resource requirements list's logical configuration. |
| [WdfIoResourceListGetDescriptor function](nf-wdfresource-wdfioresourcelistgetdescriptor.md) | The WdfIoResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a resource requirements list's logical configuration. |
| [WdfIoResourceListInsertDescriptor function](nf-wdfresource-wdfioresourcelistinsertdescriptor.md) | The WdfIoResourceListInsertDescriptor method inserts a resource descriptor into a resource requirements list's logical configuration. |
| [WdfIoResourceListRemove function](nf-wdfresource-wdfioresourcelistremove.md) | The WdfIoResourceListRemove method removes a resource descriptor from a resource requirements list's logical configuration. |
| [WdfIoResourceListRemoveByDescriptor function](nf-wdfresource-wdfioresourcelistremovebydescriptor.md) | The WdfIoResourceListRemoveByDescriptor method removes a resource descriptor from a resource requirement list's logical configuration. |
| [WdfIoResourceListUpdateDescriptor function](nf-wdfresource-wdfioresourcelistupdatedescriptor.md) | The WdfIoResourceListUpdateDescriptor method updates a resource descriptor in a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListAppendIoResList function](nf-wdfresource-wdfioresourcerequirementslistappendioreslist.md) | The WdfIoResourceRequirementsListAppendIoResList method adds a logical configuration to the end of a resource requirements list. |
| [WdfIoResourceRequirementsListGetCount function](nf-wdfresource-wdfioresourcerequirementslistgetcount.md) | The WdfIoResourceRequirementsListGetCount method returns the number of logical configurations that are contained in a resource requirements list. |
| [WdfIoResourceRequirementsListGetIoResList function](nf-wdfresource-wdfioresourcerequirementslistgetioreslist.md) | The WdfIoResourceRequirementsListGetIoResList method returns a handle to the framework resource-range-list object that represents a specified logical configuration in a specified resource requirements list. |
| [WdfIoResourceRequirementsListInsertIoResList function](nf-wdfresource-wdfioresourcerequirementslistinsertioreslist.md) | The WdfIoResourceRequirementsListInsertIoResList method inserts a logical configuration into a resource requirements list. |
| [WdfIoResourceRequirementsListRemove function](nf-wdfresource-wdfioresourcerequirementslistremove.md) | The WdfIoResourceRequirementsListRemove method removes a logical configuration from a resource requirements list. |
| [WdfIoResourceRequirementsListRemoveByIoResList function](nf-wdfresource-wdfioresourcerequirementslistremovebyioreslist.md) | The WdfIoResourceRequirementsListRemoveByIoResList method removes a logical configuration from a resource requirements list. |
| [WdfIoResourceRequirementsListSetInterfaceType function](nf-wdfresource-wdfioresourcerequirementslistsetinterfacetype.md) | The WdfIoResourceRequirementsListSetInterfaceType method assigns a bus type to a resource requirements list. |
| [WdfIoResourceRequirementsListSetSlotNumber function](nf-wdfresource-wdfioresourcerequirementslistsetslotnumber.md) | The WdfIoResourceRequirementsListSetSlotNumber method assigns a slot number to a resource requirements list. |
