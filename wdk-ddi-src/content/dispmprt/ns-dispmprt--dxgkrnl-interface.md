---
UID: NS.dispmprt._DXGKRNL_INTERFACE
title: DXGKRNL_INTERFACE
author: windows-driver-content
description: The DXGKRNL_INTERFACE structure contains a handle to a display adapter and a set of function pointers.
old-location: display\dxgkrnl_interface2.htm
old-project: display
ms.assetid: d97d3ec6-aaa5-4f4a-a39f-42c09473b18e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKRNL_INTERFACE, DXGKRNL_INTERFACE, *PDXGKRNL_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available beginning with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKRNL_INTERFACE
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

# DXGKRNL_INTERFACE structure



## -description
<p>The <b>DXGKRNL_INTERFACE</b> structure contains a handle to a display adapter and  a set of function pointers. The functions are implemented by the display port driver and called by the display miniport driver. The display port driver provides the display miniport driver with the handle and function pointers by passing a <b>DXGKRNL_INTERFACE</b> structure to <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>.</p>


## -syntax

````
typedef struct _DXGKRNL_INTERFACE {
  ULONG                                 Size;
  ULONG                                 Version;
  HANDLE                                DeviceHandle;
  DXGKCB_EVAL_ACPI_METHOD               DxgkCbEvalAcpiMethod;
  DXGKCB_GET_DEVICE_INFORMATION         DxgkCbGetDeviceInformation;
  DXGKCB_INDICATE_CHILD_STATUS          DxgkCbIndicateChildStatus;
  DXGKCB_MAP_MEMORY                     DxgkCbMapMemory;
  DXGKCB_QUEUE_DPC                      DxgkCbQueueDpc;
  DXGKCB_QUERY_SERVICES                 DxgkCbQueryServices;
  DXGKCB_READ_DEVICE_SPACE              DxgkCbReadDeviceSpace;
  DXGKCB_SYNCHRONIZE_EXECUTION          DxgkCbSynchronizeExecution;
  DXGKCB_UNMAP_MEMORY                   DxgkCbUnmapMemory;
  DXGKCB_WRITE_DEVICE_SPACE             DxgkCbWriteDeviceSpace;
  DXGKCB_IS_DEVICE_PRESENT              DxgkCbIsDevicePresent;
  DXGKCB_GETHANDLEDATA                  DxgkCbGetHandleData;
  DXGKCB_GETHANDLEPARENT                DxgkCbGetHandleParent;
  DXGKCB_ENUMHANDLECHILDREN             DxgkCbEnumHandleChildren;
  DXGKCB_NOTIFY_INTERRUPT               DxgkCbNotifyInterrupt;
  DXGKCB_NOTIFY_DPC                     DxgkCbNotifyDpc;
  DXGKCB_QUERYVIDPNINTERFACE            DxgkCbQueryVidPnInterface;
  DXGKCB_QUERYMONITORINTERFACE          DxgkCbQueryMonitorInterface;
  DXGKCB_GETCAPTUREADDRESS              DxgkCbGetCaptureAddress;
  DXGKCB_LOG_ETW_EVENT                  DxgkCbLogEtwEvent;
  DXGKCB_EXCLUDE_ADAPTER_ACCESS         DxgkCbExcludeAdapterAccess;
#if DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  DXGKCB_CREATECONTEXTALLOCATION        DxgkCbCreateContextAllocation;
  DXGKCB_DESTROYCONTEXTALLOCATION       DxgkCbDestroyContextAllocation;
  DXGKCB_SETPOWERCOMPONENTACTIVE        DxgkCbSetPowerComponentActive;
  DXGKCB_SETPOWERCOMPONENTIDLE          DxgkCbSetPowerComponentIdle;
  DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP DxgkCbAcquirePostDisplayOwnership;
  DXGKCB_POWERRUNTIMECONTROLREQUEST     DxgkCbPowerRuntimeControlRequest;
  DXGKCB_SETPOWERCOMPONENTLATENCY       DxgkCbSetPowerComponentLatency;
  DXGKCB_SETPOWERCOMPONENTRESIDENCY     DxgkCbSetPowerComponentResidency;
  DXGKCB_COMPLETEFSTATETRANSITION       DxgkCbCompleteFStateTransition;
#endif 
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3_M1)
  DXGKCB_COMPLETEPSTATETRANSITION       DxgkCbCompletePStateTransition;
#endif 
} DXGKRNL_INTERFACE, *PDXGKRNL_INTERFACE;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>An integer that indicates the size, in bytes, of this structure.</p>
</dd>

### -field Version

<dd>
<p>A positive integer that indicates the version of the functional interface implemented by the display port driver.</p>
<p>
<p>The following are the allowed values, which are defined in D3dukmdt.h.</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="DXGKDDI_INTERFACE_VERSION_VISTA"></a><a id="dxgkddi_interface_version_vista"></a><dl>

### -field DXGKDDI_INTERFACE_VERSION_VISTA

</dl>
</td>
<td width="60%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DXGKDDI_INTERFACE_VERSION_VISTA_SP1"></a><a id="dxgkddi_interface_version_vista_sp1"></a><dl>

### -field DXGKDDI_INTERFACE_VERSION_VISTA_SP1

</dl>
</td>
<td width="60%">
<p>Windows Vista with SP1</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DXGKDDI_INTERFACE_VERSION_VISTA_WIN7"></a><a id="dxgkddi_interface_version_vista_win7"></a><dl>

### -field DXGKDDI_INTERFACE_VERSION_VISTA_WIN7

</dl>
</td>
<td width="60%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DXGKDDI_INTERFACE_VERSION_WIN8"></a><a id="dxgkddi_interface_version_win8"></a><dl>

### -field DXGKDDI_INTERFACE_VERSION_WIN8

</dl>
</td>
<td width="60%">
<p>Windows 8</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field DeviceHandle

<dd>
<p>A handle, generated by the display port driver, that represents a display adapter. The display miniport driver passes the handle as an argument each time it calls any of the functions in DXGKRNL_INTERFACE.</p>
</dd>

### -field DxgkCbEvalAcpiMethod

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-eval-acpi-method.md">DxgkCbEvalAcpiMethod</a> function.</p>
</dd>

### -field DxgkCbGetDeviceInformation

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-get-device-information.md">DxgkCbGetDeviceInformation</a> function.</p>
</dd>

### -field DxgkCbIndicateChildStatus

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-indicate-child-status.md">DxgkCbIndicateChildStatus</a> function.</p>
</dd>

### -field DxgkCbMapMemory

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-map-memory.md">DxgkCbMapMemory</a> function.</p>
</dd>

### -field DxgkCbQueueDpc

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-queue-dpc.md">DxgkCbQueueDpc</a> function.</p>
</dd>

### -field DxgkCbQueryServices

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-query-services.md">DxgkCbQueryServices</a> function.</p>
</dd>

### -field DxgkCbReadDeviceSpace

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-read-device-space.md">DxgkCbReadDeviceSpace</a> function.</p>
</dd>

### -field DxgkCbSynchronizeExecution

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-synchronize-execution.md">DxgkCbSynchronizeExecution</a> function.</p>
</dd>

### -field DxgkCbUnmapMemory

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-unmap-memory.md">DxgkCbUnmapMemory</a> function.</p>
</dd>

### -field DxgkCbWriteDeviceSpace

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-write-device-space.md">DxgkCbWriteDeviceSpace</a> function.</p>
</dd>

### -field DxgkCbIsDevicePresent

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-is-device-present.md">DxgkCbIsDevicePresent</a> function.</p>
</dd>

### -field DxgkCbGetHandleData

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a> function.</p>
</dd>

### -field DxgkCbGetHandleParent

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandleparent.md">DxgkCbGetHandleParent</a> function.</p>
</dd>

### -field DxgkCbEnumHandleChildren

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-enumhandlechildren.md">DxgkCbEnumHandleChildren</a> function.</p>
</dd>

### -field DxgkCbNotifyInterrupt

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-notify-interrupt.md">DxgkCbNotifyInterrupt</a> function.</p>
</dd>

### -field DxgkCbNotifyDpc

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-notify-dpc.md">DxgkCbNotifyDpc</a> function.</p>
</dd>

### -field DxgkCbQueryVidPnInterface

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-queryvidpninterface.md">DxgkCbQueryVidPnInterface</a> function.</p>
</dd>

### -field DxgkCbQueryMonitorInterface

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-querymonitorinterface.md">DxgkCbQueryMonitorInterface</a> function.</p>
</dd>

### -field DxgkCbGetCaptureAddress

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-getcaptureaddress.md">DxgkCbGetCaptureAddress</a> function.</p>
</dd>

### -field DxgkCbLogEtwEvent

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-log-etw-event.md">DxgkCbLogEtwEvent</a> function.</p>
</dd>

### -field DxgkCbExcludeAdapterAccess

<dd>
<p>A pointer to the display port driver's <a href="..\dispmprt\nc-dispmprt-dxgkcb-exclude-adapter-access.md">DxgkCbExcludeAdapterAccess</a> function.</p>
</dd>

### -field DxgkCbCreateContextAllocation

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-createcontextallocation.md">DxgkCbCreateContextAllocation</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbDestroyContextAllocation

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-destroycontextallocation.md">DxgkCbDestroyContextAllocation</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbSetPowerComponentActive

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-setpowercomponentactive.md">DxgkCbSetPowerComponentActive</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbSetPowerComponentIdle

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-setpowercomponentidle.md">DxgkCbSetPowerComponentIdle</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbAcquirePostDisplayOwnership

<dd>
<p>A pointer to the display port driver's <a href="display.DxgkCbAcquirePostDisplayOwnership">DxgkCbAcquirePostDisplayOwnership</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbPowerRuntimeControlRequest

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-powerruntimecontrolrequest.md">DxgkCbPowerRuntimeControlRequest</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbSetPowerComponentLatency

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-setpowercomponentlatency.md">DxgkCbSetPowerComponentLatency</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbSetPowerComponentResidency

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-setpowercomponentresidency.md">DxgkCbSetPowerComponentResidency</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbCompleteFStateTransition

<dd>
<p>A pointer to the display port driver's <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-completefstatetransition.md">DxgkCbCompleteFStateTransition</a> function.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field DxgkCbCompletePStateTransition

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available beginning with Windows Vista.</p>
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
<a href="display.dxgkrnl_interface">Dxgkrnl Interface</a>
</dt>
<dt>
<a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>
</dt>
<dt>
<a href="display.driverentry_of_display_miniport_driver">DriverEntry of Display Miniport Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKRNL_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
