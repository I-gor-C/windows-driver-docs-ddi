---
UID: NS.dispmprt._DRIVER_INITIALIZATION_DATA
title: DRIVER_INITIALIZATION_DATA
author: windows-driver-content
description: The DRIVER_INITIALIZATION_DATA structure contains pointers to functions implemented by the display miniport driver.
old-location: display\driver_initialization_data.htm
old-project: display
ms.assetid: 3ab00f9c-7ce9-41bf-85c5-96be31d19719
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DRIVER_INITIALIZATION_DATA, DRIVER_INITIALIZATION_DATA, *PDRIVER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRIVER_INITIALIZATION_DATA
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

# DRIVER_INITIALIZATION_DATA structure



## -description
<p>The <b>DRIVER_INITIALIZATION_DATA</b> structure contains pointers to functions implemented by the display miniport driver. The display miniport driver's <a href="display.driverentry_of_display_miniport_driver">DriverEntry</a> function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.</p>


## -syntax

````
typedef struct _DRIVER_INITIALIZATION_DATA {
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
  PDXGKDDI_CREATEDEVICE                                   DxgkDdiCreateDevice;
  PDXGKDDI_CREATEALLOCATION                               DxgkDdiCreateAllocation;
  PDXGKDDI_DESTROYALLOCATION                              DxgkDdiDestroyAllocation;
  PDXGKDDI_DESCRIBEALLOCATION                             DxgkDdiDescribeAllocation;
  PDXGKDDI_GETSTANDARDALLOCATIONDRIVERDATA                DxgkDdiGetStandardAllocationDriverData;
  PDXGKDDI_ACQUIRESWIZZLINGRANGE                          DxgkDdiAcquireSwizzlingRange;
  PDXGKDDI_RELEASESWIZZLINGRANGE                          DxgkDdiReleaseSwizzlingRange;
  PDXGKDDI_PATCH                                          DxgkDdiPatch;
  PDXGKDDI_SUBMITCOMMAND                                  DxgkDdiSubmitCommand;
  PDXGKDDI_PREEMPTCOMMAND                                 DxgkDdiPreemptCommand;
  PDXGKDDI_BUILDPAGINGBUFFER                              DxgkDdiBuildPagingBuffer;
  PDXGKDDI_SETPALETTE                                     DxgkDdiSetPalette;
  PDXGKDDI_SETPOINTERPOSITION                             DxgkDdiSetPointerPosition;
  PDXGKDDI_SETPOINTERSHAPE                                DxgkDdiSetPointerShape;
  PDXGKDDI_RESETFROMTIMEOUT                               DxgkDdiResetFromTimeout;
  PDXGKDDI_RESTARTFROMTIMEOUT                             DxgkDdiRestartFromTimeout;
  PDXGKDDI_ESCAPE                                         DxgkDdiEscape;
  PDXGKDDI_COLLECTDBGINFO                                 DxgkDdiCollectDbgInfo;
  PDXGKDDI_QUERYCURRENTFENCE                              DxgkDdiQueryCurrentFence;
  PDXGKDDI_ISSUPPORTEDVIDPN                               DxgkDdiIsSupportedVidPn;
  PDXGKDDI_RECOMMENDFUNCTIONALVIDPN                       DxgkDdiRecommendFunctionalVidPn;
  PDXGKDDI_ENUMVIDPNCOFUNCMODALITY                        DxgkDdiEnumVidPnCofuncModality;
  PDXGKDDI_SETVIDPNSOURCEADDRESS                          DxgkDdiSetVidPnSourceAddress;
  PDXGKDDI_SETVIDPNSOURCEVISIBILITY                       DxgkDdiSetVidPnSourceVisibility;
  PDXGKDDI_COMMITVIDPN                                    DxgkDdiCommitVidPn;
  PDXGKDDI_UPDATEACTIVEVIDPNPRESENTPATH                   DxgkDdiUpdateActiveVidPnPresentPath;
  PDXGKDDI_RECOMMENDMONITORMODES                          DxgkDdiRecommendMonitorModes;
  PDXGKDDI_RECOMMENDVIDPNTOPOLOGY                         DxgkDdiRecommendVidPnTopology;
  PDXGKDDI_GETSCANLINE                                    DxgkDdiGetScanLine;
  PDXGKDDI_STOPCAPTURE                                    DxgkDdiStopCapture;
  PDXGKDDI_CONTROLINTERRUPT                               DxgkDdiControlInterrupt;
  PDXGKDDI_CREATEOVERLAY                                  DxgkDdiCreateOverlay;
  PDXGKDDI_DESTROYDEVICE                                  DxgkDdiDestroyDevice;
  PDXGKDDI_OPENALLOCATIONINFO                             DxgkDdiOpenAllocation;
  PDXGKDDI_CLOSEALLOCATION                                DxgkDdiCloseAllocation;
  PDXGKDDI_RENDER                                         DxgkDdiRender;
  PDXGKDDI_PRESENT                                        DxgkDdiPresent;
  PDXGKDDI_UPDATEOVERLAY                                  DxgkDdiUpdateOverlay;
  PDXGKDDI_FLIPOVERLAY                                    DxgkDdiFlipOverlay;
  PDXGKDDI_DESTROYOVERLAY                                 DxgkDdiDestroyOverlay;
  PDXGKDDI_CREATECONTEXT                                  DxgkDdiCreateContext;
  PDXGKDDI_DESTROYCONTEXT                                 DxgkDdiDestroyContext;
  PDXGKDDI_LINK_DEVICE                                    DxgkDdiLinkDevice;
  PDXGKDDI_SETDISPLAYPRIVATEDRIVERFORMAT                  DxgkDdiSetDisplayPrivateDriverFormat;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN7)
  PDXGKDDI_DESCRIBEPAGETABLE                              DxgkDdiDescribePageTable;
  PDXGKDDI_UPDATEPAGETABLE                                DxgkDdiUpdatePageTable;
  PDXGKDDI_UPDATEPAGEDIRECTORY                            DxgkDdiUpdatePageDirectory;
  PDXGKDDI_MOVEPAGEDIRECTORY                              DxgkDdiMovePageDirectory;
  PDXGKDDI_SUBMITRENDER                                   DxgkDdiSubmitRender;
  PDXGKDDI_CREATEALLOCATION2                              DxgkDdiCreateAllocation2;
  PDXGKDDI_RENDER                                         DxgkDdiRenderKm;
  VOID                                                    *Reserved;
  PDXGKDDI_QUERYVIDPNHWCAPABILITY                         DxgkDdiQueryVidPnHWCapability;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  PDXGKDDISETPOWERCOMPONENTFSTATE                         DxgkDdiSetPowerComponentFState;
  PDXGKDDI_QUERYDEPENDENTENGINEGROUP                      DxgkDdiQueryDependentEngineGroup;
  PDXGKDDI_QUERYENGINESTATUS                              DxgkDdiQueryEngineStatus;
  PDXGKDDI_RESETENGINE                                    DxgkDdiResetEngine;
  PDXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP DxgkDdiStopDeviceAndReleasePostDisplayOwnership;
  PDXGKDDI_SYSTEM_DISPLAY_ENABLE                          DxgkDdiSystemDisplayEnable;
  PDXGKDDI_SYSTEM_DISPLAY_WRITE                           DxgkDdiSystemDisplayWrite;
  PDXGKDDI_CANCELCOMMAND                                  DxgkDdiCancelCommand;
  PDXGKDDI_GET_CHILD_CONTAINER_ID                         DxgkDdiGetChildContainerId;
  PDXGKDDIPOWERRUNTIMECONTROLREQUEST                      DxgkDdiPowerRuntimeControlRequest;
  PDXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY     DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay;
  PDXGKDDI_NOTIFY_SURPRISE_REMOVAL                        DxgkDdiNotifySurpriseRemoval;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  PDXGKDDI_GETNODEMETADATA                                DxgkDdiGetNodeMetadata;
  PDXGKDDISETPOWERPSTATE                                  DxgkDdiSetPowerPState;
  PDXGKDDI_CONTROLINTERRUPT2                              DxgkDdiControlInterrupt2;
  PDXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT                  DxgkDdiCheckMultiPlaneOverlaySupport;
  PDXGKDDI_CALIBRATEGPUCLOCK                              DxgkDdiCalibrateGpuClock;
  PDXGKDDI_FORMATHISTORYBUFFER                            DxgkDdiFormatHistoryBuffer;
#endif 
} DRIVER_INITIALIZATION_DATA, *PDRIVER_INITIALIZATION_DATA;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>A positive integer that indicates the version of the functional interface implemented by the display miniport driver. The display miniport driver must set this member to <b>DXGKDDI_INTERFACE_VERSION</b>, which is defined in Dispmprt.h.</p>
</dd>

### -field <b>DxgkDdiAddDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiStartDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiStopDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddistopdevice">DxgkDdiStopDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiRemoveDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiremovedevice">DxgkDdiRemoveDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiDispatchIoRequest</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidispatchiorequest">DxgkDdiDispatchIoRequest</a> function.</p>
</dd>

### -field <b>DxgkDdiInterruptRoutine</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiinterruptroutine">DxgkDdiInterruptRoutine</a> function.</p>
</dd>

### -field <b>DxgkDdiDpcRoutine</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryChildRelations</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryChildStatus</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerychildstatus">DxgkDdiQueryChildStatus</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryDeviceDescriptor</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerydevicedescriptor">DxgkDdiQueryDeviceDescriptor</a> function.</p>
</dd>

### -field <b>DxgkDdiSetPowerState</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpowerstate">DxgkDdiSetPowerState</a> function.</p>
</dd>

### -field <b>DxgkDdiNotifyAcpiEvent</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddinotifyacpievent">DxgkDdiNotifyAcpiEvent</a> function.</p>
</dd>

### -field <b>DxgkDdiResetDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiresetdevice">DxgkDdiResetDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiUnload</b>

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-unload.md">DxgkDdiUnload</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryInterface</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a> function.</p>
</dd>

### -field <b>DxgkDdiControlEtwLogging</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicontroletwlogging">DxgkDdiControlEtwLogging</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryAdapterInfo</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function.</p>
</dd>

### -field <b>DxgkDdiCreateDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiCreateAllocation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function. </p>
</dd>

### -field <b>DxgkDdiDestroyAllocation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroyallocation">DxgkDdiDestroyAllocation</a> function.</p>
</dd>

### -field <b>DxgkDdiDescribeAllocation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidescribeallocation">DxgkDdiDescribeAllocation</a> function. </p>
</dd>

### -field <b>DxgkDdiGetStandardAllocationDriverData</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddigetstandardallocationdriverdata">DxgkDdiGetStandardAllocationDriverData</a> function. </p>
</dd>

### -field <b>DxgkDdiAcquireSwizzlingRange</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiacquireswizzlingrange">DxgkDdiAcquireSwizzlingRange</a> function.</p>
</dd>

### -field <b>DxgkDdiReleaseSwizzlingRange</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddireleaseswizzlingrange">DxgkDdiReleaseSwizzlingRange</a> function.</p>
</dd>

### -field <b>DxgkDdiPatch</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipatch">DxgkDdiPatch</a> function.</p>
</dd>

### -field <b>DxgkDdiSubmitCommand</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisubmitcommand">DxgkDdiSubmitCommand</a> function.</p>
</dd>

### -field <b>DxgkDdiPreemptCommand</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipreemptcommand">DxgkDdiPreemptCommand</a> function.</p>
</dd>

### -field <b>DxgkDdiBuildPagingBuffer</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> function.</p>
</dd>

### -field <b>DxgkDdiSetPalette</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpalette">DxgkDdiSetPalette</a> function that sets the palette for the display.</p>
</dd>

### -field <b>DxgkDdiSetPointerPosition</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpointerposition">DxgkDdiSetPointerPosition</a> function.</p>
</dd>

### -field <b>DxgkDdiSetPointerShape</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpointershape">DxgkDdiSetPointerShape</a> function.</p>
</dd>

### -field <b>DxgkDdiResetFromTimeout</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiresetfromtimeout">DxgkDdiResetFromTimeout</a> function.</p>
</dd>

### -field <b>DxgkDdiRestartFromTimeout</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirestartfromtimeout">DxgkDdiRestartFromTimeout</a> function.</p>
</dd>

### -field <b>DxgkDdiEscape</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiescape">DxgkDdiEscape</a> function.</p>
</dd>

### -field <b>DxgkDdiCollectDbgInfo</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicollectdbginfo">DxgkDdiCollectDbgInfo</a> function.</p>
</dd>

### -field <b>DxgkDdiQueryCurrentFence</b>

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-querycurrentfence.md">DxgkDdiQueryCurrentFence</a> function.</p>
</dd>

### -field <b>DxgkDdiIsSupportedVidPn</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a> function.</p>
</dd>

### -field <b>DxgkDdiRecommendFunctionalVidPn</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a> function.</p>
</dd>

### -field <b>DxgkDdiEnumVidPnCofuncModality</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a> function.</p>
</dd>

### -field <b>DxgkDdiSetVidPnSourceAddress</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetvidpnsourceaddress">DxgkDdiSetVidPnSourceAddress</a> function.</p>
</dd>

### -field <b>DxgkDdiSetVidPnSourceVisibility</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetvidpnsourcevisibility">DxgkDdiSetVidPnSourceVisibility</a> function.</p>
</dd>

### -field <b>DxgkDdiCommitVidPn</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicommitvidpn">DxgkDdiCommitVidPn</a>  function.</p>
</dd>

### -field <b>DxgkDdiUpdateActiveVidPnPresentPath</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a> function.</p>
</dd>

### -field <b>DxgkDdiRecommendMonitorModes</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirecommendmonitormodes">DxgkDdiRecommendMonitorModes</a> function.</p>
</dd>

### -field <b>DxgkDdiRecommendVidPnTopology</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirecommendvidpntopology">DxgkDdiRecommendVidPnTopology</a> function.</p>
</dd>

### -field <b>DxgkDdiGetScanLine</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddigetscanline">DxgkDdiGetScanLine</a> function.</p>
</dd>

### -field <b>DxgkDdiStopCapture</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddistopcapture">DxgkDdiStopCapture</a> function.</p>
</dd>

### -field <b>DxgkDdiControlInterrupt</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicontrolinterrupt">DxgkDdiControlInterrupt</a> function.</p>
</dd>

### -field <b>DxgkDdiCreateOverlay</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreateoverlay">DxgkDdiCreateOverlay</a> function.</p>
<div class="alert"><b>Note</b>  The following 5 functions are specific to the graphics context device that was created through <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a>:</div>
<div> </div>
</dd>

### -field <b>DxgkDdiDestroyDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroydevice">DxgkDdiDestroyDevice</a> function.</p>
</dd>

### -field <b>DxgkDdiOpenAllocation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiopenallocation">DxgkDdiOpenAllocation</a> function.</p>
</dd>

### -field <b>DxgkDdiCloseAllocation</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicloseallocation">DxgkDdiCloseAllocation</a> function. </p>
</dd>

### -field <b>DxgkDdiRender</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirender">DxgkDdiRender</a> function.</p>
</dd>

### -field <b>DxgkDdiPresent</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipresent">DxgkDdiPresent</a> function.</p>
<div class="alert"><b>Note</b>  The following 3 functions are specific to the overlay that was created through <a href="display.dxgkddicreateoverlay">DxgkDdiCreateOverlay</a>:</div>
<div> </div>
</dd>

### -field <b>DxgkDdiUpdateOverlay</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiupdateoverlay">DxgkDdiUpdateOverlay</a> function.</p>
</dd>

### -field <b>DxgkDdiFlipOverlay</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiflipoverlay">DxgkDdiFlipOverlay</a> function.</p>
</dd>

### -field <b>DxgkDdiDestroyOverlay</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroyoverlay">DxgkDdiDestroyOverlay</a> function.</p>
<div class="alert"><b>Note</b>  The following 2 functions are specific to supporting contexts:</div>
<div> </div>
</dd>

### -field <b>DxgkDdiCreateContext</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> function.</p>
</dd>

### -field <b>DxgkDdiDestroyContext</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroycontext">DxgkDdiDestroyContext</a> function.</p>
</dd>

### -field <b>DxgkDdiLinkDevice</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddilinkdevice">DxgkDdiLinkDevice</a> function. Be aware that this function is specific to supporting linked graphics adapters.</p>
</dd>

### -field <b>DxgkDdiSetDisplayPrivateDriverFormat</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetdisplayprivatedriverformat">DxgkDdiSetDisplayPrivateDriverFormat</a> function.</p>
<div class="alert"><b>Note</b>  The following 6 <a href="display.dispmprt_h_-_reserved">reserved functions</a> declared in Dispmrt.h are available beginning with Windows 7:</div>
<div> </div>
</dd>

### -field <b>DxgkDdiDescribePageTable</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>DxgkDdiUpdatePageTable</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>DxgkDdiUpdatePageDirectory</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>DxgkDdiMovePageDirectory</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>DxgkDdiSubmitRender</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>DxgkDdiCreateAllocation2</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
<div class="alert"><b>Note</b>  The following 3 functions are available beginning with Windows 7:</div>
<div> </div>
</dd>

### -field <b>DxgkDdiRenderKm</b>

<dd>
<p>
      A pointer to the display miniport driver's <a href="display.dxgkddirenderkm">DxgkDdiRenderKm</a> function.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field <b>DxgkDdiQueryVidPnHWCapability</b>

<dd>
<p>
      A pointer to the display miniport driver's <a href="display.dxgkddiqueryvidpnhwcapability">DxgkDdiQueryVidPnHWCapability</a> function.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
<div class="alert"><b>Note</b>  The following 12 functions, including one reserved function, are available beginning with Windows 8:</div>
<div> </div>
</dd>

### -field <b>DxgkDdiSetPowerComponentFState</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpowercomponentfstate">DxgkDdiSetPowerComponentFState</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiQueryDependentEngineGroup</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerydependentenginegroup">DxgkDdiQueryDependentEngineGroup</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiQueryEngineStatus</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiqueryenginestatus">DxgkDdiQueryEngineStatus</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiResetEngine</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiresetengine">DxgkDdiResetEngine</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiStopDeviceAndReleasePostDisplayOwnership</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddireleasepostdisplayownership">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiSystemDisplayEnable</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisystemdisplayenable">DxgkDdiSystemDisplayEnable</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiSystemDisplayWrite</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisystemdisplaywrite">DxgkDdiSystemDisplayWrite</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiCancelCommand</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicancelcommand">DxgkDdiCancelCommand</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiGetChildContainerId</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddigetchildcontainerid">DxgkDdiGetChildContainerId</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiPowerRuntimeControlRequest</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipowerruntimecontrolrequest">DxgkDdiPowerRuntimeControlRequest</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>DxgkDdiNotifySurpriseRemoval</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddinotifysurpriseremoval">DxgkDdiNotifySurpriseRemoval</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>DxgkDdiGetNodeMetadata</b>

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-getnodemetadata.md">DxgkDdiGetNodeMetadata</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>DxgkDdiSetPowerPState</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>DxgkDdiControlInterrupt2</b>

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-controlinterrupt2.md">DxgkDdiControlInterrupt2</a> function.</p>
<p>Supported starting with Windows 10</p>
</dd>

### -field <b>DxgkDdiCheckMultiPlaneOverlaySupport</b>

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-checkmultiplaneoverlaysupport.md">DxgkDdiCheckMultiPlaneOverlaySupport</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>DxgkDdiCalibrateGpuClock</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicalibrategpuclock">DxgkDdiCalibrateGpuClock</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>DxgkDdiFormatHistoryBuffer</b>

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiformathistorybuffer">DxgkDdiFormatHistoryBuffer</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks
<p>The following <b>typedef</b> declarations provide function data types from data types that are dereferenced pointers to functions:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DRIVER_INITIALIZATION_DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
