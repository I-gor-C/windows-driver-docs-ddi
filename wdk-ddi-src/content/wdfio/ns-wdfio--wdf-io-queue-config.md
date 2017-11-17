---
UID: NS.wdfio._WDF_IO_QUEUE_CONFIG
title: WDF_IO_QUEUE_CONFIG
author: windows-driver-content
description: The WDF_IO_QUEUE_CONFIG structure contains configuration information for a framework queue object.
old-location: wdf\wdf_io_queue_config.htm
ms.assetid: aa8b64a7-eae9-444c-892f-841ca5a610cf
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
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
ms.keywords: WDF_IO_QUEUE_CONFIG, WDF_IO_QUEUE_CONFIG, *PWDF_IO_QUEUE_CONFIG
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

### -field <b>Size</b>

<dd>
<p>The length, in bytes, of this structure.</p>
</dd>

### -field <b>DispatchType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552362">WDF_IO_QUEUE_DISPATCH_TYPE</a> enumerator that identifies the request dispatching type for the queue.</p>
</dd>

### -field <b>PowerManaged</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value that, if set to <b>WdfTrue</b>, indicates that the framework handles power management of the queue. </p>
<p>If set to <b>WdfFalse</b>, the driver must handle power management of the queue. </p>
<p>If set to <b>WdfDefault</b>, the framework handles power management for the queue unless the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547273">WdfFdoInitSetFilter</a>. </p>
<p>Drivers above the <a href="wdf.power_policy_ownership">power policy owner</a> in the driver stack must not set the <b>PowerManaged</b> member to <b>WdfTrue</b>. </p>
<p>For more information about power-managed I/O queues, see <a href="wdf.power_management_for_i_o_queues">Power Management for I/O Queues</a>. </p>
</dd>

### -field <b>AllowZeroLengthRequests</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the driver expects to receive read or write requests that have a buffer length of zero, so the framework delivers these requests to the driver. If <b>FALSE</b>, the framework does not deliver these requests to the driver; instead, it completes them with a completion status of STATUS_SUCCESS.</p>
</dd>

### -field <b>DefaultQueue</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the queue will be the device's <a href="wdf.creating_i_o_queues">default I/O queue</a>. If <b>FALSE</b>, the queue will not be the device's default queue.</p>
</dd>

### -field <b>EvtIoDefault</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/0b834d01-5603-43e8-9b74-9292610cc06d">EvtIoDefault</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoRead</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/d6fbb153-1355-4e94-b5d3-a218bd8c565d">EvtIoRead</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoWrite</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/5a0fa3b4-d020-4664-afa4-352573d4f079">EvtIoWrite</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoDeviceControl</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/3e3c4c53-e557-4bd1-8b7d-be59dde4b9ce">EvtIoDeviceControl</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoInternalDeviceControl</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/268d2323-57a3-4674-90e6-d7142804175b">EvtIoInternalDeviceControl</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoStop</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/71a789f1-4f10-44c3-8bd0-a0ea74ec28ab">EvtIoStop</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoResume</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/97731224-bf08-4578-958e-729acbb5a628">EvtIoResume</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtIoCanceledOnQueue</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="https://msdn.microsoft.com/1b938ee8-a5f3-4a1e-9beb-231d88aa5848">EvtIoCanceledOnQueue</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>Settings</b>

<dd>
<dl>

### -field <b>Parallel</b>

<dd>
<dl>

### -field <b>NumberOfPresentedRequests</b>

<dd>
<p>For the parallel <a href="wdf.dispatching_methods_for_i_o_requests">dispatching method</a>, the maximum number of I/O requests that the framework asynchronously delivers to the I/O queue's request handlers. For more information, see the following Remarks section. For the sequential and manual dispatching methods, this member must be zero. This member is available in version 1.9 and later versions of KMDF.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>Driver</b>

<dd>
<p>For internal use only.  Set to NULL. This member is available in version 1.11 and later versions of KMDF.
</p>
</dd>
</dl>

## -remarks
<p>The driver must initialize the <b>WDF_IO_QUEUE_CONFIG</b> structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552360">WDF_IO_QUEUE_CONFIG_INIT</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552361">WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE</a>.</p>

<p>The WDF_IO_QUEUE_CONFIG structure is used as an input parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547401">WdfIoQueueCreate</a>.</p>

<p>Beginning with version 1.9 of KMDF, drivers can use the <b>NumberOfPresentedRequests</b> member to specify the maximum number of I/O requests that the framework asynchronously delivers to a parallel I/O queue's request handlers. After the framework has delivered the specified number of I/O requests to the driver, it does not deliver more requests from the queue until the driver <a href="wdf.completing_i_o_requests">completes</a>, <a href="wdf.canceling_i_o_requests">cancels</a>, or <a href="wdf.requeuing_i_o_requests">requeues</a> at least one of the requests. </p>

<p>For parallel queues, 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552360">WDF_IO_QUEUE_CONFIG_INIT</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552361">WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE</a> set the <b>NumberOfPresentedRequests</b> member to its default value (-1), which indicates that the framework can deliver an unlimited number of I/O requests to the driver.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547401">WdfIoQueueCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552360">WDF_IO_QUEUE_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552361">WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552362">WDF_IO_QUEUE_DISPATCH_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_QUEUE_CONFIG structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
