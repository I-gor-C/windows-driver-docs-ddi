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

### -field Version

<dd>
<p>A positive integer that indicates the version of the functional interface implemented by the display miniport driver. The display miniport driver must set this member to <b>DXGKDDI_INTERFACE_VERSION</b>, which is defined in Dispmprt.h.</p>
</dd>

### -field DxgkDdiAddDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiadddevice">DxgkDdiAddDevice</a> function.</p>
</dd>

### -field DxgkDdiStartDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>

### -field DxgkDdiStopDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddistopdevice">DxgkDdiStopDevice</a> function.</p>
</dd>

### -field DxgkDdiRemoveDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiremovedevice">DxgkDdiRemoveDevice</a> function.</p>
</dd>

### -field DxgkDdiDispatchIoRequest

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidispatchiorequest">DxgkDdiDispatchIoRequest</a> function.</p>
</dd>

### -field DxgkDdiInterruptRoutine

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiinterruptroutine">DxgkDdiInterruptRoutine</a> function.</p>
</dd>

### -field DxgkDdiDpcRoutine

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidpcroutine">DxgkDdiDpcRoutine</a> function.</p>
</dd>

### -field DxgkDdiQueryChildRelations

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a> function.</p>
</dd>

### -field DxgkDdiQueryChildStatus

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerychildstatus">DxgkDdiQueryChildStatus</a> function.</p>
</dd>

### -field DxgkDdiQueryDeviceDescriptor

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerydevicedescriptor">DxgkDdiQueryDeviceDescriptor</a> function.</p>
</dd>

### -field DxgkDdiSetPowerState

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpowerstate">DxgkDdiSetPowerState</a> function.</p>
</dd>

### -field DxgkDdiNotifyAcpiEvent

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddinotifyacpievent">DxgkDdiNotifyAcpiEvent</a> function.</p>
</dd>

### -field DxgkDdiResetDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiresetdevice">DxgkDdiResetDevice</a> function.</p>
</dd>

### -field DxgkDdiUnload

<dd>
<p>A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi-unload.md">DxgkDdiUnload</a> function.</p>
</dd>

### -field DxgkDdiQueryInterface

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiqueryinterface">DxgkDdiQueryInterface</a> function.</p>
</dd>

### -field DxgkDdiControlEtwLogging

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicontroletwlogging">DxgkDdiControlEtwLogging</a> function.</p>
</dd>

### -field DxgkDdiQueryAdapterInfo

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function.</p>
</dd>

### -field DxgkDdiCreateDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a> function.</p>
</dd>

### -field DxgkDdiCreateAllocation

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function. </p>
</dd>

### -field DxgkDdiDestroyAllocation

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroyallocation">DxgkDdiDestroyAllocation</a> function.</p>
</dd>

### -field DxgkDdiDescribeAllocation

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidescribeallocation">DxgkDdiDescribeAllocation</a> function. </p>
</dd>

### -field DxgkDdiGetStandardAllocationDriverData

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddigetstandardallocationdriverdata">DxgkDdiGetStandardAllocationDriverData</a> function. </p>
</dd>

### -field DxgkDdiAcquireSwizzlingRange

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiacquireswizzlingrange">DxgkDdiAcquireSwizzlingRange</a> function.</p>
</dd>

### -field DxgkDdiReleaseSwizzlingRange

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddireleaseswizzlingrange">DxgkDdiReleaseSwizzlingRange</a> function.</p>
</dd>

### -field DxgkDdiPatch

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipatch">DxgkDdiPatch</a> function.</p>
</dd>

### -field DxgkDdiSubmitCommand

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisubmitcommand">DxgkDdiSubmitCommand</a> function.</p>
</dd>

### -field DxgkDdiPreemptCommand

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipreemptcommand">DxgkDdiPreemptCommand</a> function.</p>
</dd>

### -field DxgkDdiBuildPagingBuffer

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddibuildpagingbuffer">DxgkDdiBuildPagingBuffer</a> function.</p>
</dd>

### -field DxgkDdiSetPalette

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpalette">DxgkDdiSetPalette</a> function that sets the palette for the display.</p>
</dd>

### -field DxgkDdiSetPointerPosition

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpointerposition">DxgkDdiSetPointerPosition</a> function.</p>
</dd>

### -field DxgkDdiSetPointerShape

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpointershape">DxgkDdiSetPointerShape</a> function.</p>
</dd>

### -field DxgkDdiResetFromTimeout

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiresetfromtimeout">DxgkDdiResetFromTimeout</a> function.</p>
</dd>

### -field DxgkDdiRestartFromTimeout

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirestartfromtimeout">DxgkDdiRestartFromTimeout</a> function.</p>
</dd>

### -field DxgkDdiEscape

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiescape">DxgkDdiEscape</a> function.</p>
</dd>

### -field DxgkDdiCollectDbgInfo

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicollectdbginfo">DxgkDdiCollectDbgInfo</a> function.</p>
</dd>

### -field DxgkDdiQueryCurrentFence

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-querycurrentfence.md">DxgkDdiQueryCurrentFence</a> function.</p>
</dd>

### -field DxgkDdiIsSupportedVidPn

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a> function.</p>
</dd>

### -field DxgkDdiRecommendFunctionalVidPn

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a> function.</p>
</dd>

### -field DxgkDdiEnumVidPnCofuncModality

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a> function.</p>
</dd>

### -field DxgkDdiSetVidPnSourceAddress

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetvidpnsourceaddress">DxgkDdiSetVidPnSourceAddress</a> function.</p>
</dd>

### -field DxgkDdiSetVidPnSourceVisibility

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetvidpnsourcevisibility">DxgkDdiSetVidPnSourceVisibility</a> function.</p>
</dd>

### -field DxgkDdiCommitVidPn

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicommitvidpn">DxgkDdiCommitVidPn</a>  function.</p>
</dd>

### -field DxgkDdiUpdateActiveVidPnPresentPath

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a> function.</p>
</dd>

### -field DxgkDdiRecommendMonitorModes

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirecommendmonitormodes">DxgkDdiRecommendMonitorModes</a> function.</p>
</dd>

### -field DxgkDdiRecommendVidPnTopology

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirecommendvidpntopology">DxgkDdiRecommendVidPnTopology</a> function.</p>
</dd>

### -field DxgkDdiGetScanLine

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddigetscanline">DxgkDdiGetScanLine</a> function.</p>
</dd>

### -field DxgkDdiStopCapture

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddistopcapture">DxgkDdiStopCapture</a> function.</p>
</dd>

### -field DxgkDdiControlInterrupt

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicontrolinterrupt">DxgkDdiControlInterrupt</a> function.</p>
</dd>

### -field DxgkDdiCreateOverlay

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreateoverlay">DxgkDdiCreateOverlay</a> function.</p>
<div class="alert"><b>Note</b>  The following 5 functions are specific to the graphics context device that was created through <a href="display.dxgkddicreatedevice">DxgkDdiCreateDevice</a>:</div>
<div> </div>
</dd>

### -field DxgkDdiDestroyDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroydevice">DxgkDdiDestroyDevice</a> function.</p>
</dd>

### -field DxgkDdiOpenAllocation

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiopenallocation">DxgkDdiOpenAllocation</a> function.</p>
</dd>

### -field DxgkDdiCloseAllocation

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicloseallocation">DxgkDdiCloseAllocation</a> function. </p>
</dd>

### -field DxgkDdiRender

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddirender">DxgkDdiRender</a> function.</p>
</dd>

### -field DxgkDdiPresent

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipresent">DxgkDdiPresent</a> function.</p>
<div class="alert"><b>Note</b>  The following 3 functions are specific to the overlay that was created through <a href="display.dxgkddicreateoverlay">DxgkDdiCreateOverlay</a>:</div>
<div> </div>
</dd>

### -field DxgkDdiUpdateOverlay

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiupdateoverlay">DxgkDdiUpdateOverlay</a> function.</p>
</dd>

### -field DxgkDdiFlipOverlay

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiflipoverlay">DxgkDdiFlipOverlay</a> function.</p>
</dd>

### -field DxgkDdiDestroyOverlay

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroyoverlay">DxgkDdiDestroyOverlay</a> function.</p>
<div class="alert"><b>Note</b>  The following 2 functions are specific to supporting contexts:</div>
<div> </div>
</dd>

### -field DxgkDdiCreateContext

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> function.</p>
</dd>

### -field DxgkDdiDestroyContext

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddidestroycontext">DxgkDdiDestroyContext</a> function.</p>
</dd>

### -field DxgkDdiLinkDevice

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddilinkdevice">DxgkDdiLinkDevice</a> function. Be aware that this function is specific to supporting linked graphics adapters.</p>
</dd>

### -field DxgkDdiSetDisplayPrivateDriverFormat

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetdisplayprivatedriverformat">DxgkDdiSetDisplayPrivateDriverFormat</a> function.</p>
<div class="alert"><b>Note</b>  The following 6 <a href="display.dispmprt_h_-_reserved">reserved functions</a> declared in Dispmrt.h are available beginning with Windows 7:</div>
<div> </div>
</dd>

### -field DxgkDdiDescribePageTable

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field DxgkDdiUpdatePageTable

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field DxgkDdiUpdatePageDirectory

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field DxgkDdiMovePageDirectory

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field DxgkDdiSubmitRender

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field DxgkDdiCreateAllocation2

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
<div class="alert"><b>Note</b>  The following 3 functions are available beginning with Windows 7:</div>
<div> </div>
</dd>

### -field DxgkDdiRenderKm

<dd>
<p>
      A pointer to the display miniport driver's <a href="display.dxgkddirenderkm">DxgkDdiRenderKm</a> function.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field Reserved

<dd>
<p>
      This member is reserved and should be set to zero.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
</dd>

### -field DxgkDdiQueryVidPnHWCapability

<dd>
<p>
      A pointer to the display miniport driver's <a href="display.dxgkddiqueryvidpnhwcapability">DxgkDdiQueryVidPnHWCapability</a> function.
     </p>
<p>Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.</p>
<div class="alert"><b>Note</b>  The following 12 functions, including one reserved function, are available beginning with Windows 8:</div>
<div> </div>
</dd>

### -field DxgkDdiSetPowerComponentFState

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetpowercomponentfstate">DxgkDdiSetPowerComponentFState</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiQueryDependentEngineGroup

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiquerydependentenginegroup">DxgkDdiQueryDependentEngineGroup</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiQueryEngineStatus

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiqueryenginestatus">DxgkDdiQueryEngineStatus</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiResetEngine

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddiresetengine">DxgkDdiResetEngine</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiStopDeviceAndReleasePostDisplayOwnership

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddireleasepostdisplayownership">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiSystemDisplayEnable

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisystemdisplayenable">DxgkDdiSystemDisplayEnable</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiSystemDisplayWrite

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisystemdisplaywrite">DxgkDdiSystemDisplayWrite</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiCancelCommand

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicancelcommand">DxgkDdiCancelCommand</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiGetChildContainerId

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddigetchildcontainerid">DxgkDdiGetChildContainerId</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiPowerRuntimeControlRequest

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddipowerruntimecontrolrequest">DxgkDdiPowerRuntimeControlRequest</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field DxgkDdiNotifySurpriseRemoval

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddinotifysurpriseremoval">DxgkDdiNotifySurpriseRemoval</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkDdiGetNodeMetadata

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-getnodemetadata.md">DxgkDdiGetNodeMetadata</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field DxgkDdiSetPowerPState

<dd>
<p>This member is reserved and should be set to zero.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field DxgkDdiControlInterrupt2

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-controlinterrupt2.md">DxgkDdiControlInterrupt2</a> function.</p>
<p>Supported starting with Windows 10</p>
</dd>

### -field DxgkDdiCheckMultiPlaneOverlaySupport

<dd>
<p>A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-checkmultiplaneoverlaysupport.md">DxgkDdiCheckMultiPlaneOverlaySupport</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field DxgkDdiCalibrateGpuClock

<dd>
<p>A pointer to the display miniport driver's <a href="display.dxgkddicalibrategpuclock">DxgkDdiCalibrateGpuClock</a> function.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field DxgkDdiFormatHistoryBuffer

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
