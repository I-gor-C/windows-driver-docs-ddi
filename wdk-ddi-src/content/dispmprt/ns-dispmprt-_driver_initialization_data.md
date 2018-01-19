---
UID : NS:dispmprt._DRIVER_INITIALIZATION_DATA
title : _DRIVER_INITIALIZATION_DATA
author : windows-driver-content
description : The DRIVER_INITIALIZATION_DATA structure contains pointers to functions implemented by the display miniport driver.
old-location : display\driver_initialization_data.htm
old-project : display
ms.assetid : 3ab00f9c-7ce9-41bf-85c5-96be31d19719
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DRIVER_INITIALIZATION_DATA, DRIVER_INITIALIZATION_DATA, *PDRIVER_INITIALIZATION_DATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dispmprt.h
req.include-header : Dispmprt.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DRIVER_INITIALIZATION_DATA
req.alt-loc : Dispmprt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DRIVER_INITIALIZATION_DATA, *PDRIVER_INITIALIZATION_DATA
---

# _DRIVER_INITIALIZATION_DATA structure
The <b>DRIVER_INITIALIZATION_DATA</b> structure contains pointers to functions implemented by the display miniport driver. The display miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> function provides the Microsoft DirectX graphics kernel subsystem with entry points by filling in the members of this structure.

## Syntax
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

## Members

        
            `DxgkDdiAcquireSwizzlingRange`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_acquireswizzlingrange.md">DxgkDdiAcquireSwizzlingRange</a> function.
        
            `DxgkDdiAddDevice`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_add_device.md">DxgkDdiAddDevice</a> function.
        
            `DxgkDdiBuildPagingBuffer`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a> function.
        
            `DxgkDdiCalibrateGpuClock`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_calibrategpuclock.md">DxgkDdiCalibrateGpuClock</a> function.

Supported starting with Windows 8.1.
        
            `DxgkDdiCancelCommand`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_cancelcommand.md">DxgkDdiCancelCommand</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiCheckMultiPlaneOverlaySupport`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport.md">DxgkDdiCheckMultiPlaneOverlaySupport</a> function.

Supported starting with Windows 8.1.
        
            `DxgkDdiCloseAllocation`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_closeallocation.md">DxgkDdiCloseAllocation</a> function.
        
            `DxgkDdiCollectDbgInfo`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_collectdbginfo.md">DxgkDdiCollectDbgInfo</a> function.
        
            `DxgkDdiCommitVidPn`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_commitvidpn.md">DxgkDdiCommitVidPn</a>  function.
        
            `DxgkDdiControlEtwLogging`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_control_etw_logging.md">DxgkDdiControlEtwLogging</a> function.
        
            `DxgkDdiControlInterrupt`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_controlinterrupt.md">DxgkDdiControlInterrupt</a> function.
        
            `DxgkDdiControlInterrupt2`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_controlinterrupt2.md">DxgkDdiControlInterrupt2</a> function.

Supported starting with Windows 10
        
            `DxgkDdiCreateAllocation`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createallocation.md">DxgkDdiCreateAllocation</a> function.
        
            `DxgkDdiCreateAllocation2`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.

<div class="alert"><b>Note</b>  The following 3 functions are available beginning with Windows 7:</div>
<div> </div>
        
            `DxgkDdiCreateContext`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createcontext.md">DxgkDdiCreateContext</a> function.
        
            `DxgkDdiCreateDevice`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createdevice.md">DxgkDdiCreateDevice</a> function.
        
            `DxgkDdiCreateOverlay`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createoverlay.md">DxgkDdiCreateOverlay</a> function.

<div class="alert"><b>Note</b>  The following 5 functions are specific to the graphics context device that was created through <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createdevice.md">DxgkDdiCreateDevice</a>:</div>
<div> </div>
        
            `DxgkDdiDescribeAllocation`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_describeallocation.md">DxgkDdiDescribeAllocation</a> function.
        
            `DxgkDdiDescribePageTable`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `DxgkDdiDestroyAllocation`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_destroyallocation.md">DxgkDdiDestroyAllocation</a> function.
        
            `DxgkDdiDestroyContext`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_destroycontext.md">DxgkDdiDestroyContext</a> function.
        
            `DxgkDdiDestroyDevice`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_destroydevice.md">DxgkDdiDestroyDevice</a> function.
        
            `DxgkDdiDestroyOverlay`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_destroyoverlay.md">DxgkDdiDestroyOverlay</a> function.

<div class="alert"><b>Note</b>  The following 2 functions are specific to supporting contexts:</div>
<div> </div>
        
            `DxgkDdiDispatchIoRequest`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_dispatch_io_request.md">DxgkDdiDispatchIoRequest</a> function.
        
            `DxgkDdiDpcRoutine`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_dpc_routine.md">DxgkDdiDpcRoutine</a> function.
        
            `DxgkDdiEnumVidPnCofuncModality`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality.md">DxgkDdiEnumVidPnCofuncModality</a> function.
        
            `DxgkDdiEscape`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_escape.md">DxgkDdiEscape</a> function.
        
            `DxgkDdiFlipOverlay`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_flipoverlay.md">DxgkDdiFlipOverlay</a> function.
        
            `DxgkDdiFormatHistoryBuffer`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_formathistorybuffer.md">DxgkDdiFormatHistoryBuffer</a> function.

Supported starting with Windows 8.1.
        
            `DxgkDdiGetChildContainerId`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_get_child_container_id.md">DxgkDdiGetChildContainerId</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiGetNodeMetadata`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_getnodemetadata.md">DxgkDdiGetNodeMetadata</a> function.

Supported starting with Windows 8.1.
        
            `DxgkDdiGetScanLine`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_getscanline.md">DxgkDdiGetScanLine</a> function.
        
            `DxgkDdiGetStandardAllocationDriverData`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata.md">DxgkDdiGetStandardAllocationDriverData</a> function.
        
            `DxgkDdiInterruptRoutine`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_interrupt_routine.md">DxgkDdiInterruptRoutine</a> function.
        
            `DxgkDdiIsSupportedVidPn`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_issupportedvidpn.md">DxgkDdiIsSupportedVidPn</a> function.
        
            `DxgkDdiLinkDevice`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_link_device.md">DxgkDdiLinkDevice</a> function. Be aware that this function is specific to supporting linked graphics adapters.
        
            `DxgkDdiMovePageDirectory`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `DxgkDdiNotifyAcpiEvent`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_notify_acpi_event.md">DxgkDdiNotifyAcpiEvent</a> function.
        
            `DxgkDdiNotifySurpriseRemoval`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_notify_surprise_removal.md">DxgkDdiNotifySurpriseRemoval</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiOpenAllocation`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_openallocationinfo.md">DxgkDdiOpenAllocation</a> function.
        
            `DxgkDdiPatch`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_patch.md">DxgkDdiPatch</a> function.
        
            `DxgkDdiPowerRuntimeControlRequest`

            A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/56535128-3107-4fb5-b0e1-2e913c386cc2">DxgkDdiPowerRuntimeControlRequest</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiPreemptCommand`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_preemptcommand.md">DxgkDdiPreemptCommand</a> function.
        
            `DxgkDdiPresent`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_present.md">DxgkDdiPresent</a> function.

<div class="alert"><b>Note</b>  The following 3 functions are specific to the overlay that was created through <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createoverlay.md">DxgkDdiCreateOverlay</a>:</div>
<div> </div>
        
            `DxgkDdiQueryAdapterInfo`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a> function.
        
            `DxgkDdiQueryChildRelations`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_query_child_relations.md">DxgkDdiQueryChildRelations</a> function.
        
            `DxgkDdiQueryChildStatus`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_query_child_status.md">DxgkDdiQueryChildStatus</a> function.
        
            `DxgkDdiQueryCurrentFence`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_querycurrentfence.md">DxgkDdiQueryCurrentFence</a> function.
        
            `DxgkDdiQueryDependentEngineGroup`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_querydependentenginegroup.md">DxgkDdiQueryDependentEngineGroup</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiQueryDeviceDescriptor`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_query_device_descriptor.md">DxgkDdiQueryDeviceDescriptor</a> function.
        
            `DxgkDdiQueryEngineStatus`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryenginestatus.md">DxgkDdiQueryEngineStatus</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiQueryInterface`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_query_interface.md">DxgkDdiQueryInterface</a> function.
        
            `DxgkDdiQueryVidPnHWCapability`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryvidpnhwcapability.md">DxgkDdiQueryVidPnHWCapability</a> function.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.

<div class="alert"><b>Note</b>  The following 12 functions, including one reserved function, are available beginning with Windows 8:</div>
<div> </div>
        
            `DxgkDdiRecommendFunctionalVidPn`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn.md">DxgkDdiRecommendFunctionalVidPn</a> function.
        
            `DxgkDdiRecommendMonitorModes`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_recommendmonitormodes.md">DxgkDdiRecommendMonitorModes</a> function.
        
            `DxgkDdiRecommendVidPnTopology`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_recommendvidpntopology.md">DxgkDdiRecommendVidPnTopology</a> function.
        
            `DxgkDdiReleaseSwizzlingRange`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_releaseswizzlingrange.md">DxgkDdiReleaseSwizzlingRange</a> function.
        
            `DxgkDdiRemoveDevice`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_remove_device.md">DxgkDdiRemoveDevice</a> function.
        
            `DxgkDdiRender`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_render.md">DxgkDdiRender</a> function.
        
            `DxgkDdiRenderKm`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_renderkm.md">DxgkDdiRenderKm</a> function.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `DxgkDdiResetDevice`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_reset_device.md">DxgkDdiResetDevice</a> function.
        
            `DxgkDdiResetEngine`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_resetengine.md">DxgkDdiResetEngine</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiResetFromTimeout`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_resetfromtimeout.md">DxgkDdiResetFromTimeout</a> function.
        
            `DxgkDdiRestartFromTimeout`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_restartfromtimeout.md">DxgkDdiRestartFromTimeout</a> function.
        
            `DxgkDdiSetDisplayPrivateDriverFormat`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setdisplayprivatedriverformat.md">DxgkDdiSetDisplayPrivateDriverFormat</a> function.

<div class="alert"><b>Note</b>  The following 6 <a href="https://msdn.microsoft.com/F92F15A7-439D-4D45-84EE-A92D1E6AD779">reserved functions</a> declared in Dispmrt.h are available beginning with Windows 7:</div>
<div> </div>
        
            `DxgkDdiSetPalette`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setpalette.md">DxgkDdiSetPalette</a> function that sets the palette for the display.
        
            `DxgkDdiSetPointerPosition`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setpointerposition.md">DxgkDdiSetPointerPosition</a> function.
        
            `DxgkDdiSetPointerShape`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setpointershape.md">DxgkDdiSetPointerShape</a> function.
        
            `DxgkDdiSetPowerComponentFState`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddisetpowercomponentfstate.md">DxgkDdiSetPowerComponentFState</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiSetPowerPState`

            This member is reserved and should be set to zero.

Supported starting with Windows 8.1.
        
            `DxgkDdiSetPowerState`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_set_power_state.md">DxgkDdiSetPowerState</a> function.
        
            `DxgkDdiSetVidPnSourceAddress`

            A pointer to the display miniport driver's <a href="https://msdn.microsoft.com/488c929b-3816-457f-b5c2-c176b93d5546">DxgkDdiSetVidPnSourceAddress</a> function.
        
            `DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setvidpnsourceaddresswithmultiplaneoverlay.md">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> function.

Supported starting with Windows 8.1.
        
            `DxgkDdiSetVidPnSourceVisibility`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_setvidpnsourcevisibility.md">DxgkDdiSetVidPnSourceVisibility</a> function.
        
            `DxgkDdiStartDevice`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_start_device.md">DxgkDdiStartDevice</a> function.
        
            `DxgkDdiStopCapture`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_stopcapture.md">DxgkDdiStopCapture</a> function.
        
            `DxgkDdiStopDevice`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_stop_device.md">DxgkDdiStopDevice</a> function.
        
            `DxgkDdiStopDeviceAndReleasePostDisplayOwnership`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_stop_device_and_release_post_display_ownership.md">DxgkDdiStopDeviceAndReleasePostDisplayOwnership</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiSubmitCommand`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_submitcommand.md">DxgkDdiSubmitCommand</a> function.
        
            `DxgkDdiSubmitRender`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `DxgkDdiSystemDisplayEnable`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_system_display_enable.md">DxgkDdiSystemDisplayEnable</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiSystemDisplayWrite`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_system_display_write.md">DxgkDdiSystemDisplayWrite</a> function.

Supported starting with Windows 8.
        
            `DxgkDdiUnload`

            A pointer to the display miniport driver's <a href="..\dispmprt\nc-dispmprt-dxgkddi_unload.md">DxgkDdiUnload</a> function.
        
            `DxgkDdiUpdateActiveVidPnPresentPath`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath.md">DxgkDdiUpdateActiveVidPnPresentPath</a> function.
        
            `DxgkDdiUpdateOverlay`

            A pointer to the display miniport driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_updateoverlay.md">DxgkDdiUpdateOverlay</a> function.
        
            `DxgkDdiUpdatePageDirectory`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `DxgkDdiUpdatePageTable`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `Reserved`

            This member is reserved and should be set to zero.
     

Available only when DXGKDDI_INTERFACE_VERSION ≥ DXGKDDI_INTERFACE_VERSION_WIN7.
        
            `Version`

            A positive integer that indicates the version of the functional interface implemented by the display miniport driver. The display miniport driver must set this member to <b>DXGKDDI_INTERFACE_VERSION</b>, which is defined in Dispmprt.h.

    ## Remarks
        The following <b>typedef</b> declarations provide function data types from data types that are dereferenced pointers to functions:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dispmprt.h (include Dispmprt.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556157">DriverEntry of Display Miniport Driver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DRIVER_INITIALIZATION_DATA structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>