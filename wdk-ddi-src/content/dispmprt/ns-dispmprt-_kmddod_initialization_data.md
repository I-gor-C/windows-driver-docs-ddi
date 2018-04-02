---
UID: NS:dispmprt._KMDDOD_INITIALIZATION_DATA
title: "_KMDDOD_INITIALIZATION_DATA"
author: windows-driver-content
description: Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's DriverEntry function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.
old-location: display\kmddod_initialization_data.htm
old-project: display
ms.assetid: 04c1ece1-1c8f-40eb-8437-ac2fe1445095
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PKMDDOD_INITIALIZATION_DATA, KMDDOD_INITIALIZATION_DATA, KMDDOD_INITIALIZATION_DATA structure [Display Devices], PKMDDOD_INITIALIZATION_DATA, PKMDDOD_INITIALIZATION_DATA structure pointer [Display Devices], _KMDDOD_INITIALIZATION_DATA, display.kmddod_initialization_data, dispmprt/KMDDOD_INITIALIZATION_DATA, dispmprt/PKMDDOD_INITIALIZATION_DATA"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Dispmprt.h
api_name:
-	KMDDOD_INITIALIZATION_DATA
product: Windows
targetos: Windows
req.typenames: KMDDOD_INITIALIZATION_DATA, *PKMDDOD_INITIALIZATION_DATA
---

# _KMDDOD_INITIALIZATION_DATA structure
Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.

## Syntax
```
typedef struct _KMDDOD_INITIALIZATION_DATA {
  ULONG                                                   Version;
  PDXGKDDI_ADD_DEVICE                                     DxgkDdiAddDevice;
  PDXGKDDI_START_DEVICE                                   DxgkDdiStartDevice;
  PDXGKDDI_STOP_DEVICE                                    DxgkDdiStopDevice;
  PDXGKDDI_REMOVE_DEVICE                                  DxgkDdiRemoveDevice;
  PDXGKDDI_DISPATCH_IO_REQUEST                            DxgkDdiDispatchIoRequest;
  PDXGKDDI_INTERRUPT_ROUTINE                              DxgkDdiInterruptRoutine;
  PDXGKDDI_DPC_ROUTINE                                    DxgkDdiDpcRoutine;
  PDXGKDDI_QUERY_CHILD_RELATIONS                          DxgkDdiQueryChildRelations;
  PDXGKDDI_QUERY_CHILD_STATUS                             DxgkDdiQueryChildStatus;
  PDXGKDDI_QUERY_DEVICE_DESCRIPTOR                        DxgkDdiQueryDeviceDescriptor;
  PDXGKDDI_SET_POWER_STATE                                DxgkDdiSetPowerState;
  PDXGKDDI_NOTIFY_ACPI_EVENT                              DxgkDdiNotifyAcpiEvent;
  PDXGKDDI_RESET_DEVICE                                   DxgkDdiResetDevice;
  PDXGKDDI_UNLOAD                                         DxgkDdiUnload;
  PDXGKDDI_QUERY_INTERFACE                                DxgkDdiQueryInterface;
  PDXGKDDI_CONTROL_ETW_LOGGING                            DxgkDdiControlEtwLogging;
  PDXGKDDI_QUERYADAPTERINFO                               DxgkDdiQueryAdapterInfo;
  PDXGKDDI_SETPALETTE                                     DxgkDdiSetPalette;
  PDXGKDDI_SETPOINTERPOSITION                             DxgkDdiSetPointerPosition;
  PDXGKDDI_SETPOINTERSHAPE                                DxgkDdiSetPointerShape;
  PDXGKDDI_ESCAPE                                         DxgkDdiEscape;
  PDXGKDDI_COLLECTDBGINFO                                 DxgkDdiCollectDbgInfo;
  PDXGKDDI_ISSUPPORTEDVIDPN                               DxgkDdiIsSupportedVidPn;
  PDXGKDDI_RECOMMENDFUNCTIONALVIDPN                       DxgkDdiRecommendFunctionalVidPn;
  PDXGKDDI_ENUMVIDPNCOFUNCMODALITY                        DxgkDdiEnumVidPnCofuncModality;
  PDXGKDDI_SETVIDPNSOURCEVISIBILITY                       DxgkDdiSetVidPnSourceVisibility;
  PDXGKDDI_COMMITVIDPN                                    DxgkDdiCommitVidPn;
  PDXGKDDI_UPDATEACTIVEVIDPNPRESENTPATH                   DxgkDdiUpdateActiveVidPnPresentPath;
  PDXGKDDI_RECOMMENDMONITORMODES                          DxgkDdiRecommendMonitorModes;
  PDXGKDDI_GETSCANLINE                                    DxgkDdiGetScanLine;
  PDXGKDDI_QUERYVIDPNHWCAPABILITY                         DxgkDdiQueryVidPnHWCapability;
  PDXGKDDI_PRESENTDISPLAYONLY                             DxgkDdiPresentDisplayOnly;
  PDXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP DxgkDdiStopDeviceAndReleasePostDisplayOwnership;
  PDXGKDDI_SYSTEM_DISPLAY_ENABLE                          DxgkDdiSystemDisplayEnable;
  PDXGKDDI_SYSTEM_DISPLAY_WRITE                           DxgkDdiSystemDisplayWrite;
  PDXGKDDI_GET_CHILD_CONTAINER_ID                         DxgkDdiGetChildContainerId;
  PDXGKDDI_CONTROLINTERRUPT                               DxgkDdiControlInterrupt;
  PDXGKDDISETPOWERCOMPONENTFSTATE                         DxgkDdiSetPowerComponentFState;
  PDXGKDDIPOWERRUNTIMECONTROLREQUEST                      DxgkDdiPowerRuntimeControlRequest;
  PDXGKDDI_NOTIFY_SURPRISE_REMOVAL                        DxgkDdiNotifySurpriseRemoval;
  PDXGKDDI_POWERRUNTIMESETDEVICEHANDLE                    DxgkDdiPowerRuntimeSetDeviceHandle;
} *PKMDDOD_INITIALIZATION_DATA, KMDDOD_INITIALIZATION_DATA;
```

## Members


`Version`

A positive integer that indicates the version of the functional interface implemented by the KMDOD. The KMDOD must set this member to <b>DXGKDDI_INTERFACE_VERSION</b>, which is defined in Dispmprt.h.

`DxgkDdiAddDevice`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function.

`DxgkDdiStartDevice`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a> function.

`DxgkDdiStopDevice`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/3c17c7cf-9cfa-421d-a503-88726519fb6c">DxgkDdiStopDevice</a> function.

`DxgkDdiRemoveDevice`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/0d5f96e8-dcb3-49e5-8347-ba20d757618b">DxgkDdiRemoveDevice</a> function.

`DxgkDdiDispatchIoRequest`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e1973aca-cbc2-4780-a3b5-7601e1cc6c90">DxgkDdiDispatchIoRequest</a> function.

`DxgkDdiInterruptRoutine`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a> function.

<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>

`DxgkDdiDpcRoutine`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/2767906a-f084-4ccc-b24f-ba7d66c96477">DxgkDdiDpcRoutine</a> function.

<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>

`DxgkDdiQueryChildRelations`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/eb1a0df0-6239-4d82-8477-7dd015f80b6e">DxgkDdiQueryChildRelations</a> function.

`DxgkDdiQueryChildStatus`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/478e0c52-4324-4062-8e1e-381808b0f481">DxgkDdiQueryChildStatus</a> function.

`DxgkDdiQueryDeviceDescriptor`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/0dfcc012-9fff-40b6-b71f-da2ca229896c">DxgkDdiQueryDeviceDescriptor</a> function.

`DxgkDdiSetPowerState`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/6462be4f-1f6e-4b85-a3ba-15820ee8605b">DxgkDdiSetPowerState</a> function.

`DxgkDdiNotifyAcpiEvent`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/fdefde51-0e90-4324-9c14-e8259fc872b3">DxgkDdiNotifyAcpiEvent</a> function.

`DxgkDdiResetDevice`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e757e63d-6d78-4b20-9471-290f56c1bcde">DxgkDdiResetDevice</a> function.

`DxgkDdiUnload`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/336fa87a-6c3e-4337-90d9-b0ebeb355e68">DxgkDdiUnload</a> function.

`DxgkDdiQueryInterface`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/d8255f36-be3a-4b19-ac8d-8748ac9b6a24">DxgkDdiQueryInterface</a> function.

`DxgkDdiControlEtwLogging`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/c94a43bb-19d0-4894-80b0-885562fefea5">DxgkDdiControlEtwLogging</a> function.

`DxgkDdiQueryAdapterInfo`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

`DxgkDdiSetPalette`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/3a46bf84-df62-4247-b842-d5b131c96428">DxgkDdiSetPalette</a> function that sets the palette for the display.

`DxgkDdiSetPointerPosition`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/b30e4f19-068c-4ab0-a2e9-b1f57592be1c">DxgkDdiSetPointerPosition</a> function.

`DxgkDdiSetPointerShape`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/36b462f7-5bad-4716-8138-af00d20e945b">DxgkDdiSetPointerShape</a> function.

`DxgkDdiEscape`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/79a524cd-dec1-4ea8-a660-d9d9c644e162">DxgkDdiEscape</a> function.

`DxgkDdiCollectDbgInfo`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/f2f3d8f7-5a54-4830-b8f8-ac2f93096eda">DxgkDdiCollectDbgInfo</a> function.

`DxgkDdiIsSupportedVidPn`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/96e96366-6306-4d20-8752-e942f2ed4069">DxgkDdiIsSupportedVidPn</a> function.

`DxgkDdiRecommendFunctionalVidPn`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/320a77a7-d7d4-47b9-8a40-2b6e12819e4b">DxgkDdiRecommendFunctionalVidPn</a> function.

`DxgkDdiEnumVidPnCofuncModality`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/6dda82bd-1a43-4ffe-b398-a9f8cee6d1c1">DxgkDdiEnumVidPnCofuncModality</a> function.

`DxgkDdiSetVidPnSourceVisibility`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/c94473b4-b898-456d-944d-8879adea16d1">DxgkDdiSetVidPnSourceVisibility</a> function.

`DxgkDdiCommitVidPn`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a>  function.

`DxgkDdiUpdateActiveVidPnPresentPath`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/3bf5ebf7-8113-4ab2-beb1-1a52df25ac37">DxgkDdiUpdateActiveVidPnPresentPath</a> function.

`DxgkDdiRecommendMonitorModes`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/1fa29ab6-1faa-4be6-ae87-4cac9057471d">DxgkDdiRecommendMonitorModes</a> function.

`DxgkDdiGetScanLine`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e37bb3c6-a0b6-409f-8a82-20ec7a931c6a">DxgkDdiGetScanLine</a> function.

<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>

`DxgkDdiQueryVidPnHWCapability`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/41af9528-4497-41aa-a65d-70352aa85f8c">DxgkDdiQueryVidPnHWCapability</a> function.

`DxgkDdiPresentDisplayOnly`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/41af9528-4497-41aa-a65d-70352aa85f8c">DxgkDdiQueryVidPnHWCapability</a> function.

`DxgkDdiStopDeviceAndReleasePostDisplayOwnership`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/6AF170BF-C422-4340-8935-31A4D4F3EFA5">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.

`DxgkDdiSystemDisplayEnable`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/D938F7F4-E1FA-4C63-A31D-5ED160276565">DxgkDdiSystemDisplayEnable</a> function.

`DxgkDdiSystemDisplayWrite`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/5C0F9878-522C-4DDE-A790-54C94880F119">DxgkDdiSystemDisplayWrite</a> function.

`DxgkDdiGetChildContainerId`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e7073fb3-0cb7-425e-9ffb-d7eaa963a70f">DxgkDdiGetChildContainerId</a> function.

`DxgkDdiControlInterrupt`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/d6bef242-bafc-4d9e-a729-d62ccdbd2667">DxgkDdiControlInterrupt</a> function.

<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>

`DxgkDdiSetPowerComponentFState`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/C68CC6F1-83D6-43D9-93F3-99E3A990C7D7">DxgkDdiSetPowerComponentFState</a> function.

`DxgkDdiPowerRuntimeControlRequest`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a> function.

`DxgkDdiNotifySurpriseRemoval`

A pointer to the KMDOD's <a href="https://msdn.microsoft.com/4e6403e7-7463-479a-8be9-4136287b375e">DxgkDdiNotifySurpriseRemoval</a> function.

`DxgkDdiPowerRuntimeSetDeviceHandle`



## Remarks
If the kernel mode display-only driver (KMDOD) supports the VSync control feature, it must implement all of the  <a href="https://msdn.microsoft.com/d6bef242-bafc-4d9e-a729-d62ccdbd2667">DxgkDdiControlInterrupt</a>, <a href="https://msdn.microsoft.com/e37bb3c6-a0b6-409f-8a82-20ec7a931c6a">DxgkDdiGetScanLine</a>, <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a>, and <a href="https://msdn.microsoft.com/2767906a-f084-4ccc-b24f-ba7d66c96477">DxgkDdiDpcRoutine</a>  functions and must provide valid function pointers to all of these functions in this structure. Conversely, if the KMDOD does not support the VSync control feature, it must not implement either <i>DxgkDdiControlInterrupt</i> or <i>DxgkDdiGetScanLine</i>  functions and must not provide valid function pointers to either of these functions in this structure. For more information, see <a href="https://msdn.microsoft.com/d7ee7461-0d2a-4103-9225-57ca10a75a7a">Saving Energy with VSync Control</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff556157">DriverEntry of Display Miniport Driver</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh463972">DxgkInitializeDisplayOnlyDriver</a>