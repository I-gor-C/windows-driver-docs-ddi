---
UID: NS.dispmprt._KMDDOD_INITIALIZATION_DATA
title: KMDDOD_INITIALIZATION_DATA
author: windows-driver-content
description: Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's DriverEntry function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.
old-location: display\kmddod_initialization_data.htm
old-project: display
ms.assetid: 04c1ece1-1c8f-40eb-8437-ac2fe1445095
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: KMDDOD_INITIALIZATION_DATA, KMDDOD_INITIALIZATION_DATA, *PKMDDOD_INITIALIZATION_DATA
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
req.iface: 
---

# KMDDOD_INITIALIZATION_DATA structure



## -description
<p>Contains pointers to functions implemented by a kernel mode display-only driver (KMDOD). The KMDOD's <a href="display.driverentry_of_display_miniport_driver">DriverEntry</a> function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.</p>


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

### -field Version

<dd>
<p>A positive integer that indicates the version of the functional interface implemented by the KMDOD. The KMDOD must set this member to <b>DXGKDDI_INTERFACE_VERSION</b>, which is defined in Dispmprt.h.</p>
</dd>

### -field DxgkDdiAddDevice

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function.</p>
</dd>

### -field DxgkDdiStartDevice

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>

### -field DxgkDdiStopDevice

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddistopdevice">DxgkDdiStopDevice</a> function.</p>
</dd>

### -field DxgkDdiRemoveDevice

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiremovedevice">DxgkDdiRemoveDevice</a> function.</p>
</dd>

### -field DxgkDdiDispatchIoRequest

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddidispatchiorequest">DxgkDdiDispatchIoRequest</a> function.</p>
</dd>

### -field DxgkDdiInterruptRoutine

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiinterruptroutine">DxgkDdiInterruptRoutine</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field DxgkDdiDpcRoutine

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field DxgkDdiQueryChildRelations

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a> function.</p>
</dd>

### -field DxgkDdiQueryChildStatus

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiquerychildstatus">DxgkDdiQueryChildStatus</a> function.</p>
</dd>

### -field DxgkDdiQueryDeviceDescriptor

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiquerydevicedescriptor">DxgkDdiQueryDeviceDescriptor</a> function.</p>
</dd>

### -field DxgkDdiSetPowerState

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddisetpowerstate">DxgkDdiSetPowerState</a> function.</p>
</dd>

### -field DxgkDdiNotifyAcpiEvent

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddinotifyacpievent">DxgkDdiNotifyAcpiEvent</a> function.</p>
</dd>

### -field DxgkDdiResetDevice

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiresetdevice">DxgkDdiResetDevice</a> function.</p>
</dd>

### -field DxgkDdiUnload

<dd>
<p>A pointer to the KMDOD's <a href="..\dispmprt\nc-dispmprt-dxgkddi-unload.md">DxgkDdiUnload</a> function.</p>
</dd>

### -field DxgkDdiQueryInterface

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a> function.</p>
</dd>

### -field DxgkDdiControlEtwLogging

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddicontroletwlogging">DxgkDdiControlEtwLogging</a> function.</p>
</dd>

### -field DxgkDdiQueryAdapterInfo

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function.</p>
</dd>

### -field DxgkDdiSetPalette

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddisetpalette">DxgkDdiSetPalette</a> function that sets the palette for the display.</p>
</dd>

### -field DxgkDdiSetPointerPosition

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddisetpointerposition">DxgkDdiSetPointerPosition</a> function.</p>
</dd>

### -field DxgkDdiSetPointerShape

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddisetpointershape">DxgkDdiSetPointerShape</a> function.</p>
</dd>

### -field DxgkDdiEscape

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiescape">DxgkDdiEscape</a> function.</p>
</dd>

### -field DxgkDdiCollectDbgInfo

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddicollectdbginfo">DxgkDdiCollectDbgInfo</a> function.</p>
</dd>

### -field DxgkDdiIsSupportedVidPn

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a> function.</p>
</dd>

### -field DxgkDdiRecommendFunctionalVidPn

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a> function.</p>
</dd>

### -field DxgkDdiEnumVidPnCofuncModality

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a> function.</p>
</dd>

### -field DxgkDdiSetVidPnSourceVisibility

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddisetvidpnsourcevisibility">DxgkDdiSetVidPnSourceVisibility</a> function.</p>
</dd>

### -field DxgkDdiCommitVidPn

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddicommitvidpn">DxgkDdiCommitVidPn</a>  function.</p>
</dd>

### -field DxgkDdiUpdateActiveVidPnPresentPath

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a> function.</p>
</dd>

### -field DxgkDdiRecommendMonitorModes

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddirecommendmonitormodes">DxgkDdiRecommendMonitorModes</a> function.</p>
</dd>

### -field DxgkDdiGetScanLine

<dd>
<p>A pointer to the KMDOD's <a href="display.dxgkddigetscanline">DxgkDdiGetScanLine</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field DxgkDdiQueryVidPnHWCapability

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddiqueryvidpnhwcapability">DxgkDdiQueryVidPnHWCapability</a> function.</p>
</dd>

### -field DxgkDdiPresentDisplayOnly

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddiqueryvidpnhwcapability">DxgkDdiQueryVidPnHWCapability</a> function.</p>
</dd>

### -field DxgkDdiStopDeviceAndReleasePostDisplayOwnership

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddireleasepostdisplayownership">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.</p>
</dd>

### -field DxgkDdiSystemDisplayEnable

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddisystemdisplayenable">DxgkDdiSystemDisplayEnable</a> function.</p>
</dd>

### -field DxgkDdiSystemDisplayWrite

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddisystemdisplaywrite">DxgkDdiSystemDisplayWrite</a> function.</p>
</dd>

### -field DxgkDdiGetChildContainerId

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddigetchildcontainerid">DxgkDdiGetChildContainerId</a> function.</p>
</dd>

### -field DxgkDdiControlInterrupt

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddicontrolinterrupt">DxgkDdiControlInterrupt</a> function.</p>
<div class="alert"><b>Note</b>  This function pointer has special requirements. For more information, see Remarks.</div>
<div> </div>
</dd>

### -field DxgkDdiSetPowerComponentFState

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddisetpowercomponentfstate">DxgkDdiSetPowerComponentFState</a> function.</p>
</dd>

### -field DxgkDdiPowerRuntimeControlRequest

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddipowerruntimecontrolrequest">DxgkDdiPowerRuntimeControlRequest</a> function.</p>
</dd>

### -field DxgkDdiNotifySurpriseRemoval

<dd>
<p>
      A pointer to the KMDOD's <a href="display.dxgkddinotifysurpriseremoval">DxgkDdiNotifySurpriseRemoval</a> function.</p>
</dd>
</dl>

## -remarks
<p>If the kernel mode display-only driver (KMDOD) supports the VSync control feature, it must implement all of the  <a href="display.dxgkddicontrolinterrupt">DxgkDdiControlInterrupt</a>, <a href="display.dxgkddigetscanline">DxgkDdiGetScanLine</a>, <a href="display.dxgkddiinterruptroutine">DxgkDdiInterruptRoutine</a>, and <a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a>  functions and must provide valid function pointers to all of these functions in this structure. Conversely, if the KMDOD does not support the VSync control feature, it must not implement either <i>DxgkDdiControlInterrupt</i> or <i>DxgkDdiGetScanLine</i>  functions and must not provide valid function pointers to either of these functions in this structure. For more information, see <a href="https://msdn.microsoft.com/d7ee7461-0d2a-4103-9225-57ca10a75a7a">Saving Energy with VSync Control</a>.</p>

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
<a href="display.driverentry_of_display_miniport_driver">DriverEntry of Display Miniport Driver</a>
</dt>
<dt>
<a href="..\dispmprt\nf-dispmprt-dxgkinitializedisplayonlydriver.md">DxgkInitializeDisplayOnlyDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20KMDDOD_INITIALIZATION_DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
