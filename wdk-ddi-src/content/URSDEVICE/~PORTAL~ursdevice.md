# Declarations in the ursdevice header
This header Ursdevice contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_URSSETHARDWAREEVENTSUPPORT callback function](nc-ursdevice-pfn-urssethardwareeventsupport.md) | TBD |
| [PFN_URSDEVICEINITINITIALIZE callback function](nc-ursdevice-pfn-ursdeviceinitinitialize.md) | TBD |
| [PFN_URSDEVICEINITIALIZE callback function](nc-ursdevice-pfn-ursdeviceinitialize.md) | TBD |
| [EVT_URS_SET_ROLE callback function](nc-ursdevice-evt-urs-set-role.md) | TBD |
| [PFN_URSSETPOHANDLE callback function](nc-ursdevice-pfn-urssetpohandle.md) | TBD |
| [PFN_URSREPORTHARDWAREEVENT callback function](nc-ursdevice-pfn-ursreporthardwareevent.md) | TBD |
| [PFN_URSIORESOURCELISTAPPENDDESCRIPTOR callback function](nc-ursdevice-pfn-ursioresourcelistappenddescriptor.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UrsDeviceInitialize function](nf-ursdevice-ursdeviceinitialize.md) | Initializes a framework device object to support operations related to a USB dual-role controller and registers the relevant event callback functions with the USB dual-role controller class extension. |
| [UrsDeviceInitInitialize function](nf-ursdevice-ursdeviceinitinitialize.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
| [UrsReportHardwareEvent function](nf-ursdevice-ursreporthardwareevent.md) | Notifies the USB dual-role class extension about a new hardware event. |
| [UrsIoResourceListAppendDescriptor function](nf-ursdevice-ursioresourcelistappenddescriptor.md) | Appends the specified resource descriptor to the specified I/O resource list object that maintains resource descriptors for the host or function role. |
| [UrsSetPoHandle function](nf-ursdevice-urssetpohandle.md) | Registers and deletes the client driver's registration with the power management framework (PoFx). |
| [URS_CONFIG_INIT function](nf-ursdevice-urs-config-init.md) | Initializes a URS_CONFIG structure. |
| [UrsSetHardwareEventSupport function](nf-ursdevice-urssethardwareeventsupport.md) | Indicates the client driver's support for reporting new hardware events. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [URS_CONFIG structure](ns-ursdevice--urs-config.md) | Contains pointers to event callback functions implemented by the URS client driver for a USB dual-role controller. Initialize this structure by calling URS_CONFIG_INIT. |

This header is used in these topics:

- [usbref](..content/_usbref)
