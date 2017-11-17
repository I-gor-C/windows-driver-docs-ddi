---
UID: NS.dispmprt._KMDDOD_INITIALIZATION_DATA
title: KMDDOD_INITIALIZATION_DATA
author: windows-driver-content
description: Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's DriverEntry function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.
old-location: display\kmddod_initialization_data.htm
ms.assetid: 04c1ece1-1c8f-40eb-8437-ac2fe1445095
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KMDDOD_INITIALIZATION_DATA
req.alt-loc: Dispmprt.h
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
ms.keywords: KMDDOD_INITIALIZATION_DATA, KMDDOD_INITIALIZATION_DATA, *PKMDDOD_INITIALIZATION_DATA
req.iface: 
---

# KMDDOD_INITIALIZATION_DATA structure



## -description
<p>Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.</p>


## -syntax

````
typedef struct _KMDDOD_INITIALIZATION_DATA {
  ULONG                                                   Version;
  PDXGKDDI_ADD_DEVICE                                     DxgkDdiAddDevice;
  PDXGKDDI_START_DEVICE                                   DxgkDdiStartDevice;
  PDXGKDDI_STOP_DEVICE                                    DxgkDdiStopDevice;
  PDXGKDDI_REMOVE_DEVICE                                  DxgkDdiRemoveDevice;
  PDXGKDDI_DISPATCH_IO_REQUEST                            DxgkDdiDispatchIoRequest;
  PDXGKDDI_INTERRUPT_ROUTINE                              DxgkDdiInterruptRoutine;
  PDXGKDDI_DPC_ROUTINE                                    DxgkDdiDpcRoutine;
  PDXGKDDI_QUERY_CHILD_RELATIONS                          DxgkDdiQueryChildRelations;
  PDXGKDDI_QUERY_CHILD_STATUS                             DxgkDdiQueryChildStatus;
  PDXGKDDI_QUERY_DEVICE_DESCRIPTOR                        DxgkDdiQueryDeviceDescriptor;
  PDXGKDDI_SET_POWER_STATE                                DxgkDdiSetPowerState;
  PDXGKDDI_NOTIFY_ACPI_EVENT                              DxgkDdiNotifyAcpiEvent;
  PDXGKDDI_RESET_DEVICE                                   DxgkDdiResetDevice;
  PDXGKDDI_UNLOAD                                         DxgkDdiUnload;
  PDXGKDDI_QUERY_INTERFACE                                DxgkDdiQueryInterface;
  PDXGKDDI_CONTROL_ETW_LOGGING                            DxgkDdiControlEtwLogging;
  PDXGKDDI_QUERYADAPTERINFO                               DxgkDdiQueryAdapterInfo;
  PDXGKDDI_SETPALETTE                                     DxgkDdiSetPalette;
  PDXGKDDI_SETPOINTERPOSITION                             DxgkDdiSetPointerPosition;
  PDXGKDDI_SETPOINTERSHAPE                                DxgkDdiSetPointerShape;
  PDXGKDDI_ESCAPE                                         DxgkDdiEscape;
  PDXGKDDI_COLLECTDBGINFO                                 DxgkDdiCollectDbgInfo;
  PDXGKDDI_ISSUPPORTEDVIDPN                               DxgkDdiIsSupportedVidPn;
  PDXGKDDI_RECOMMENDFUNCTIONALVIDPN                       DxgkDdiRecommendFunctionalVidPn;
  PDXGKDDI_ENUMVIDPNCOFUNCMODALITY                        DxgkDdiEnumVidPnCofuncModality;
  PDXGKDDI_SETVIDPNSOURCEVISIBILITY                       DxgkDdiSetVidPnSourceVisibility;
  PDXGKDDI_COMMITVIDPN                                    DxgkDdiCommitVidPn;
  PDXGKDDI_UPDATEACTIVEVIDPNPRESENTPATH                   DxgkDdiUpdateActiveVidPnPresentPath;
  PDXGKDDI_RECOMMENDMONITORMODES                          DxgkDdiRecommendMonitorModes;
  PDXGKDDI_GETSCANLINE                                    DxgkDdiGetScanLine;
  PDXGKDDI_QUERYVIDPNHWCAPABILITY                         DxgkDdiQueryVidPnHWCapability;
  PDXGKDDI_PRESENTDISPLAYONLY                             DxgkDdiPresentDisplayOnly;
  PDXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP DxgkDdiStopDeviceAndReleasePostDisplayOwnership;
  PDXGKDDI_SYSTEM_DISPLAY_ENABLE                          DxgkDdiSystemDisplayEnable;
  PDXGKDDI_SYSTEM_DISPLAY_WRITE                           DxgkDdiSystemDisplayWrite;
  PDXGKDDI_GET_CHILD_CONTAINER_ID                         DxgkDdiGetChildContainerId;
  PDXGKDDI_CONTROLINTERRUPT                               DxgkDdiControlInterrupt;
  PDXGKDDISETPOWERCOMPONENTFSTATE                         DxgkDdiSetPowerComponentFState;
  PDXGKDDIPOWERRUNTIMECONTROLREQUEST                      DxgkDdiPowerRuntimeControlRequest;
  PDXGKDDI_NOTIFY_SURPRISE_REMOVAL                        DxgkDdiNotifySurpriseRemoval;
} KMDDOD_INITIALIZATION_DATA, *PKMDDOD_INITIALIZATION_DATA;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>A positive integer that indicates the version of the functional interface implemented by the KMDOD. The KMDOD must set this member to <b>DXGKDDI_INTERFACE_VERSION</b>, which is defined in Dispmprt.h.</p>
</dd>

### -field <b>DxgkDdiAddDevice</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiStartDevice</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiStopDevice</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/3c17c7cf-9cfa-421d-a503-88726519fb6c">DxgkDdiStopDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiRemoveDevice</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/0d5f96e8-dcb3-49e5-8347-ba20d757618b">DxgkDdiRemoveDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiDispatchIoRequest</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e1973aca-cbc2-4780-a3b5-7601e1cc6c90">DxgkDdiDispatchIoRequest</a> function.</p>
</dd>

### -field <b>DxgkDdiInterruptRoutine</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field <b>DxgkDdiDpcRoutine</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/2767906a-f084-4ccc-b24f-ba7d66c96477">DxgkDdiDpcRoutine</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field <b>DxgkDdiQueryChildRelations</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/eb1a0df0-6239-4d82-8477-7dd015f80b6e">DxgkDdiQueryChildRelations</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryChildStatus</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/478e0c52-4324-4062-8e1e-381808b0f481">DxgkDdiQueryChildStatus</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryDeviceDescriptor</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/0dfcc012-9fff-40b6-b71f-da2ca229896c">DxgkDdiQueryDeviceDescriptor</a> function.</p>
</dd>

### -field <b>DxgkDdiSetPowerState</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/6462be4f-1f6e-4b85-a3ba-15820ee8605b">DxgkDdiSetPowerState</a> function.</p>
</dd>

### -field <b>DxgkDdiNotifyAcpiEvent</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/fdefde51-0e90-4324-9c14-e8259fc872b3">DxgkDdiNotifyAcpiEvent</a> function.</p>
</dd>

### -field <b>DxgkDdiResetDevice</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e757e63d-6d78-4b20-9471-290f56c1bcde">DxgkDdiResetDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiUnload</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/336fa87a-6c3e-4337-90d9-b0ebeb355e68">DxgkDdiUnload</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryInterface</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/d8255f36-be3a-4b19-ac8d-8748ac9b6a24">DxgkDdiQueryInterface</a> function.</p>
</dd>

### -field <b>DxgkDdiControlEtwLogging</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/c94a43bb-19d0-4894-80b0-885562fefea5">DxgkDdiControlEtwLogging</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryAdapterInfo</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.</p>
</dd>

### -field <b>DxgkDdiSetPalette</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/3a46bf84-df62-4247-b842-d5b131c96428">DxgkDdiSetPalette</a> function that sets the palette for the display.</p>
</dd>

### -field <b>DxgkDdiSetPointerPosition</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/b30e4f19-068c-4ab0-a2e9-b1f57592be1c">DxgkDdiSetPointerPosition</a> function.</p>
</dd>

### -field <b>DxgkDdiSetPointerShape</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/36b462f7-5bad-4716-8138-af00d20e945b">DxgkDdiSetPointerShape</a> function.</p>
</dd>

### -field <b>DxgkDdiEscape</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/79a524cd-dec1-4ea8-a660-d9d9c644e162">DxgkDdiEscape</a> function.</p>
</dd>

### -field <b>DxgkDdiCollectDbgInfo</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/f2f3d8f7-5a54-4830-b8f8-ac2f93096eda">DxgkDdiCollectDbgInfo</a> function.</p>
</dd>

### -field <b>DxgkDdiIsSupportedVidPn</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/96e96366-6306-4d20-8752-e942f2ed4069">DxgkDdiIsSupportedVidPn</a> function.</p>
</dd>

### -field <b>DxgkDdiRecommendFunctionalVidPn</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/320a77a7-d7d4-47b9-8a40-2b6e12819e4b">DxgkDdiRecommendFunctionalVidPn</a> function.</p>
</dd>

### -field <b>DxgkDdiEnumVidPnCofuncModality</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/6dda82bd-1a43-4ffe-b398-a9f8cee6d1c1">DxgkDdiEnumVidPnCofuncModality</a> function.</p>
</dd>

### -field <b>DxgkDdiSetVidPnSourceVisibility</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/c94473b4-b898-456d-944d-8879adea16d1">DxgkDdiSetVidPnSourceVisibility</a> function.</p>
</dd>

### -field <b>DxgkDdiCommitVidPn</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a>  function.</p>
</dd>

### -field <b>DxgkDdiUpdateActiveVidPnPresentPath</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/3bf5ebf7-8113-4ab2-beb1-1a52df25ac37">DxgkDdiUpdateActiveVidPnPresentPath</a> function.</p>
</dd>

### -field <b>DxgkDdiRecommendMonitorModes</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/1fa29ab6-1faa-4be6-ae87-4cac9057471d">DxgkDdiRecommendMonitorModes</a> function.</p>
</dd>

### -field <b>DxgkDdiGetScanLine</b>

<dd>
<p>A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e37bb3c6-a0b6-409f-8a82-20ec7a931c6a">DxgkDdiGetScanLine</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field <b>DxgkDdiQueryVidPnHWCapability</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/41af9528-4497-41aa-a65d-70352aa85f8c">DxgkDdiQueryVidPnHWCapability</a> function.</p>
</dd>

### -field <b>DxgkDdiPresentDisplayOnly</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/41af9528-4497-41aa-a65d-70352aa85f8c">DxgkDdiQueryVidPnHWCapability</a> function.</p>
</dd>

### -field <b>DxgkDdiStopDeviceAndReleasePostDisplayOwnership</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/6AF170BF-C422-4340-8935-31A4D4F3EFA5">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.</p>
</dd>

### -field <b>DxgkDdiSystemDisplayEnable</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/D938F7F4-E1FA-4C63-A31D-5ED160276565">DxgkDdiSystemDisplayEnable</a> function.</p>
</dd>

### -field <b>DxgkDdiSystemDisplayWrite</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/5C0F9878-522C-4DDE-A790-54C94880F119">DxgkDdiSystemDisplayWrite</a> function.</p>
</dd>

### -field <b>DxgkDdiGetChildContainerId</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/e7073fb3-0cb7-425e-9ffb-d7eaa963a70f">DxgkDdiGetChildContainerId</a> function.</p>
</dd>

### -field <b>DxgkDdiControlInterrupt</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/d6bef242-bafc-4d9e-a729-d62ccdbd2667">DxgkDdiControlInterrupt</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field <b>DxgkDdiSetPowerComponentFState</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/C68CC6F1-83D6-43D9-93F3-99E3A990C7D7">DxgkDdiSetPowerComponentFState</a> function.</p>
</dd>

### -field <b>DxgkDdiPowerRuntimeControlRequest</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a> function.</p>
</dd>

### -field <b>DxgkDdiNotifySurpriseRemoval</b>

<dd>
<p>
      A pointer to the KMDOD's <a href="https://msdn.microsoft.com/4e6403e7-7463-479a-8be9-4136287b375e">DxgkDdiNotifySurpriseRemoval</a> function.</p>
</dd>
</dl>

## -remarks
<p>If the kernel mode display-only driver (KMDOD) supports the VSync control feature, it must implement all of the  <a href="https://msdn.microsoft.com/d6bef242-bafc-4d9e-a729-d62ccdbd2667">DxgkDdiControlInterrupt</a>, <a href="https://msdn.microsoft.com/e37bb3c6-a0b6-409f-8a82-20ec7a931c6a">DxgkDdiGetScanLine</a>, <a href="https://msdn.microsoft.com/eacfd42d-405c-4c23-8978-0f373a393e10">DxgkDdiInterruptRoutine</a>, and <a href="https://msdn.microsoft.com/2767906a-f084-4ccc-b24f-ba7d66c96477">DxgkDdiDpcRoutine</a>  functions and must provide valid function pointers to all of these functions in this structure. Conversely, if the KMDOD does not support the VSync control feature, it must not implement either <i>DxgkDdiControlInterrupt</i> or <i>DxgkDdiGetScanLine</i>  functions and must not provide valid function pointers to either of these functions in this structure. For more information, see <a href="https://msdn.microsoft.com/d7ee7461-0d2a-4103-9225-57ca10a75a7a">Saving Energy with VSync Control</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556157">DriverEntry of Display Miniport Driver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh463972">DxgkInitializeDisplayOnlyDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20KMDDOD_INITIALIZATION_DATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
