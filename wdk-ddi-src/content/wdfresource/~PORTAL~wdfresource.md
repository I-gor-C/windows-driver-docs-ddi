# Declarations in the wdfresource header
This header Wdfresource contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfIoResourceRequirementsListGetIoResList function](nf-wdfresource-wdfioresourcerequirementslistgetioreslist.md) | The WdfIoResourceRequirementsListGetIoResList method returns a handle to the framework resource-range-list object that represents a specified logical configuration in a specified resource requirements list. |
| [WdfIoResourceRequirementsListSetSlotNumber function](nf-wdfresource-wdfioresourcerequirementslistsetslotnumber.md) | The WdfIoResourceRequirementsListSetSlotNumber method assigns a slot number to a resource requirements list. |
| [WdfCmResourceListGetDescriptor function](nf-wdfresource-wdfcmresourcelistgetdescriptor.md) | The WdfCmResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a specified resource list. |
| [WdfCmResourceListAppendDescriptor function](nf-wdfresource-wdfcmresourcelistappenddescriptor.md) | The WdfCmResourceListAppendDescriptor method adds a resource descriptor to the end of a specified resource list. |
| [WdfIoResourceListRemoveByDescriptor function](nf-wdfresource-wdfioresourcelistremovebydescriptor.md) | The WdfIoResourceListRemoveByDescriptor method removes a resource descriptor from a resource requirement list's logical configuration. |
| [WdfIoResourceRequirementsListInsertIoResList function](nf-wdfresource-wdfioresourcerequirementslistinsertioreslist.md) | The WdfIoResourceRequirementsListInsertIoResList method inserts a logical configuration into a resource requirements list. |
| [WdfCmResourceListGetCount function](nf-wdfresource-wdfcmresourcelistgetcount.md) | The WdfCmResourceListGetCount method returns the number of resource descriptors that are contained in a specified resource list. |
| [WdfIoResourceListCreate function](nf-wdfresource-wdfioresourcelistcreate.md) | The WdfIoResourceListCreate method creates an empty logical configuration, which can be populated and added to a resource requirements list. |
| [WdfIoResourceListRemove function](nf-wdfresource-wdfioresourcelistremove.md) | The WdfIoResourceListRemove method removes a resource descriptor from a resource requirements list's logical configuration. |
| [WdfCmResourceListRemove function](nf-wdfresource-wdfcmresourcelistremove.md) | The WdfCmResourceListRemove method removes a resource descriptor from a specified resource list. |
| [WdfIoResourceListGetDescriptor function](nf-wdfresource-wdfioresourcelistgetdescriptor.md) | The WdfIoResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a resource requirements list's logical configuration. |
| [WdfCmResourceListRemoveByDescriptor function](nf-wdfresource-wdfcmresourcelistremovebydescriptor.md) | The WdfCmResourceListRemoveByDescriptor method removes a specified resource descriptor from a specified resource list. |
| [WdfIoResourceListGetCount function](nf-wdfresource-wdfioresourcelistgetcount.md) | The WdfIoResourceListGetCount method returns the number of resource descriptors that are contained in a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListGetCount function](nf-wdfresource-wdfioresourcerequirementslistgetcount.md) | The WdfIoResourceRequirementsListGetCount method returns the number of logical configurations that are contained in a resource requirements list. |
| [WdfIoResourceListAppendDescriptor function](nf-wdfresource-wdfioresourcelistappenddescriptor.md) | The WdfIoResourceListAppendDescriptor method adds a resource descriptor to the end of a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListAppendIoResList function](nf-wdfresource-wdfioresourcerequirementslistappendioreslist.md) | The WdfIoResourceRequirementsListAppendIoResList method adds a logical configuration to the end of a resource requirements list. |
| [WdfIoResourceListInsertDescriptor function](nf-wdfresource-wdfioresourcelistinsertdescriptor.md) | The WdfIoResourceListInsertDescriptor method inserts a resource descriptor into a resource requirements list's logical configuration. |
| [WdfCmResourceListInsertDescriptor function](nf-wdfresource-wdfcmresourcelistinsertdescriptor.md) | The WdfCmResourceListInsertDescriptor method inserts a resource descriptor into a specified resource list. |
| [WdfIoResourceRequirementsListRemoveByIoResList function](nf-wdfresource-wdfioresourcerequirementslistremovebyioreslist.md) | The WdfIoResourceRequirementsListRemoveByIoResList method removes a logical configuration from a resource requirements list. |
| [WdfIoResourceRequirementsListSetInterfaceType function](nf-wdfresource-wdfioresourcerequirementslistsetinterfacetype.md) | The WdfIoResourceRequirementsListSetInterfaceType method assigns a bus type to a resource requirements list. |
| [WdfIoResourceListUpdateDescriptor function](nf-wdfresource-wdfioresourcelistupdatedescriptor.md) | The WdfIoResourceListUpdateDescriptor method updates a resource descriptor in a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListRemove function](nf-wdfresource-wdfioresourcerequirementslistremove.md) | The WdfIoResourceRequirementsListRemove method removes a logical configuration from a resource requirements list. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFIORESOURCELISTUPDATEDESCRIPTOR callback function](nc-wdfresource-pfn-wdfioresourcelistupdatedescriptor.md) | TBD |
| [PFN_WDFCMRESOURCELISTAPPENDDESCRIPTOR callback function](nc-wdfresource-pfn-wdfcmresourcelistappenddescriptor.md) | TBD |
| [PFN_WDFIORESOURCELISTINSERTDESCRIPTOR callback function](nc-wdfresource-pfn-wdfioresourcelistinsertdescriptor.md) | TBD |
| [PFN_WDFIORESOURCELISTGETCOUNT callback function](nc-wdfresource-pfn-wdfioresourcelistgetcount.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistsetslotnumber.md) | TBD |
| [PFN_WDFIORESOURCELISTREMOVEBYDESCRIPTOR callback function](nc-wdfresource-pfn-wdfioresourcelistremovebydescriptor.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVEBYIORESLIST callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistremovebyioreslist.md) | TBD |
| [PFN_WDFCMRESOURCELISTREMOVE callback function](nc-wdfresource-pfn-wdfcmresourcelistremove.md) | TBD |
| [PFN_WDFCMRESOURCELISTGETDESCRIPTOR callback function](nc-wdfresource-pfn-wdfcmresourcelistgetdescriptor.md) | TBD |
| [PFN_WDFCMRESOURCELISTINSERTDESCRIPTOR callback function](nc-wdfresource-pfn-wdfcmresourcelistinsertdescriptor.md) | TBD |
| [PFN_WDFCMRESOURCELISTREMOVEBYDESCRIPTOR callback function](nc-wdfresource-pfn-wdfcmresourcelistremovebydescriptor.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTINSERTIORESLIST callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistinsertioreslist.md) | TBD |
| [PFN_WDFIORESOURCELISTAPPENDDESCRIPTOR callback function](nc-wdfresource-pfn-wdfioresourcelistappenddescriptor.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTREMOVE callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistremove.md) | TBD |
| [PFN_WDFCMRESOURCELISTGETCOUNT callback function](nc-wdfresource-pfn-wdfcmresourcelistgetcount.md) | TBD |
| [PFN_WDFIORESOURCELISTREMOVE callback function](nc-wdfresource-pfn-wdfioresourcelistremove.md) | TBD |
| [PFN_WDFIORESOURCELISTGETDESCRIPTOR callback function](nc-wdfresource-pfn-wdfioresourcelistgetdescriptor.md) | TBD |
| [PFN_WDFIORESOURCELISTCREATE callback function](nc-wdfresource-pfn-wdfioresourcelistcreate.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTGETCOUNT callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistgetcount.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTGETIORESLIST callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistgetioreslist.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTSETINTERFACETYPE callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistsetinterfacetype.md) | TBD |
| [PFN_WDFIORESOURCEREQUIREMENTSLISTAPPENDIORESLIST callback function](nc-wdfresource-pfn-wdfioresourcerequirementslistappendioreslist.md) | TBD |

This header is used in these topics:

- [wdf](..content/_wdf)
