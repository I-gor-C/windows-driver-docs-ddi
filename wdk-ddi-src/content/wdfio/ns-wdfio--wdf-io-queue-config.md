---
UID: NS.wdfio._WDF_IO_QUEUE_CONFIG
title: WDF_IO_QUEUE_CONFIG
author: windows-driver-content
description: The WDF_IO_QUEUE_CONFIG structure contains configuration information for a framework queue object.
old-location: wdf\wdf_io_queue_config.htm
old-project: wdf
ms.assetid: aa8b64a7-eae9-444c-892f-841ca5a610cf
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_IO_QUEUE_CONFIG, WDF_IO_QUEUE_CONFIG, *PWDF_IO_QUEUE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_IO_QUEUE_CONFIG
req.alt-loc: wdfio.h
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
req.product: Windows 10 or later.
---

# WDF_IO_QUEUE_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_QUEUE_CONFIG</b> structure contains configuration information for a framework queue object.</p>


## -syntax

````
typedef struct _WDF_IO_QUEUE_CONFIG {
  ULONG                                       Size;
  WDF_IO_QUEUE_DISPATCH_TYPE                  DispatchType;
  WDF_TRI_STATE                               PowerManaged;
  BOOLEAN                                     AllowZeroLengthRequests;
  BOOLEAN                                     DefaultQueue;
  PFN_WDF_IO_QUEUE_IO_DEFAULT                 EvtIoDefault;
  PFN_WDF_IO_QUEUE_IO_READ                    EvtIoRead;
  PFN_WDF_IO_QUEUE_IO_WRITE                   EvtIoWrite;
  PFN_WDF_IO_QUEUE_IO_DEVICE_CONTROL          EvtIoDeviceControl;
  PFN_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL EvtIoInternalDeviceControl;
  PFN_WDF_IO_QUEUE_IO_STOP                    EvtIoStop;
  PFN_WDF_IO_QUEUE_IO_RESUME                  EvtIoResume;
  PFN_WDF_IO_QUEUE_IO_CANCELED_ON_QUEUE       EvtIoCanceledOnQueue;
  union {
    struct {
      ULONG NumberOfPresentedRequests;
    } Parallel;
  } Settings;
  WDFDRIVER                                   Driver;
} WDF_IO_QUEUE_CONFIG, *PWDF_IO_QUEUE_CONFIG;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The length, in bytes, of this structure.</p>
</dd>

### -field DispatchType

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-io-queue-dispatch-type.md">WDF_IO_QUEUE_DISPATCH_TYPE</a> enumerator that identifies the request dispatching type for the queue.</p>
</dd>

### -field PowerManaged

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-tri-state.md">WDF_TRI_STATE</a>-typed value that, if set to <b>WdfTrue</b>, indicates that the framework handles power management of the queue. </p>
<p>If set to <b>WdfFalse</b>, the driver must handle power management of the queue. </p>
<p>If set to <b>WdfDefault</b>, the framework handles power management for the queue unless the driver calls <a href="..\wdffdo\nf-wdffdo-wdffdoinitsetfilter.md">WdfFdoInitSetFilter</a>. </p>
<p>Drivers above the <a href="wdf.power_policy_ownership">power policy owner</a> in the driver stack must not set the <b>PowerManaged</b> member to <b>WdfTrue</b>. </p>
<p>For more information about power-managed I/O queues, see <a href="wdf.power_management_for_i_o_queues">Power Management for I/O Queues</a>. </p>
</dd>

### -field AllowZeroLengthRequests

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the driver expects to receive read or write requests that have a buffer length of zero, so the framework delivers these requests to the driver. If <b>FALSE</b>, the framework does not deliver these requests to the driver; instead, it completes them with a completion status of STATUS_SUCCESS.</p>
</dd>

### -field DefaultQueue

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the queue will be the device's <a href="wdf.creating_i_o_queues">default I/O queue</a>. If <b>FALSE</b>, the queue will not be the device's default queue.</p>
</dd>

### -field EvtIoDefault

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-default.md">EvtIoDefault</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoRead

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-read.md">EvtIoRead</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoWrite

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-write.md">EvtIoWrite</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoDeviceControl

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-device-control.md">EvtIoDeviceControl</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoInternalDeviceControl

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-internal-device-control.md">EvtIoInternalDeviceControl</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoStop

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md">EvtIoStop</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoResume

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md">EvtIoResume</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field EvtIoCanceledOnQueue

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-canceled-on-queue.md">EvtIoCanceledOnQueue</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field Settings

<dd>
<dl>

### -field Parallel

<dd>
<dl>

### -field NumberOfPresentedRequests

<dd>
<p>For the parallel <a href="wdf.dispatching_methods_for_i_o_requests">dispatching method</a>, the maximum number of I/O requests that the framework asynchronously delivers to the I/O queue's request handlers. For more information, see the following Remarks section. For the sequential and manual dispatching methods, this member must be zero. This member is available in version 1.9 and later versions of KMDF.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field Driver

<dd>
<p>For internal use only.  Set to NULL. This member is available in version 1.11 and later versions of KMDF.
</p>
</dd>
</dl>

## -remarks
<p>The driver must initialize the <b>WDF_IO_QUEUE_CONFIG</b> structure by calling <a href="..\wdfio\nf-wdfio-wdf-io-queue-config-init.md">WDF_IO_QUEUE_CONFIG_INIT</a> or <a href="..\wdfio\nf-wdfio-wdf-io-queue-config-init-default-queue.md">WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE</a>.</p>

<p>The WDF_IO_QUEUE_CONFIG structure is used as an input parameter to <a href="..\wdfio\nf-wdfio-wdfioqueuecreate.md">WdfIoQueueCreate</a>.</p>

<p>Beginning with version 1.9 of KMDF, drivers can use the <b>NumberOfPresentedRequests</b> member to specify the maximum number of I/O requests that the framework asynchronously delivers to a parallel I/O queue's request handlers. After the framework has delivered the specified number of I/O requests to the driver, it does not deliver more requests from the queue until the driver <a href="wdf.completing_i_o_requests">completes</a>, <a href="wdf.canceling_i_o_requests">cancels</a>, or <a href="wdf.requeuing_i_o_requests">requeues</a> at least one of the requests. </p>

<p>For parallel queues, 
     <a href="..\wdfio\nf-wdfio-wdf-io-queue-config-init.md">WDF_IO_QUEUE_CONFIG_INIT</a> and <a href="..\wdfio\nf-wdfio-wdf-io-queue-config-init-default-queue.md">WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE</a> set the <b>NumberOfPresentedRequests</b> member to its default value (-1), which indicates that the framework can deliver an unlimited number of I/O requests to the driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfio\nf-wdfio-wdfioqueuecreate.md">WdfIoQueueCreate</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdf-io-queue-config-init.md">WDF_IO_QUEUE_CONFIG_INIT</a>
</dt>
<dt>
<a href="..\wdfio\nf-wdfio-wdf-io-queue-config-init-default-queue.md">WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-io-queue-dispatch-type.md">WDF_IO_QUEUE_DISPATCH_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_QUEUE_CONFIG structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
