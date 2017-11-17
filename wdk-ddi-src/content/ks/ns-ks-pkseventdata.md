---
UID: NS.ks.PKSEVENTDATA
title: PKSEVENTDATA
author: windows-driver-content
description: Kernel streaming clients send the KSEVENTDATA structure to the class driver to specify a notification method.
old-location: stream\kseventdata.htm
ms.assetid: 83503353-e4f7-47ba-9a0c-71264798e983
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENTDATA
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PKSEVENTDATA, KSEVENTDATA, *PKSEVENTDATA
req.iface: 
---

# PKSEVENTDATA structure



## -description
<p>Kernel streaming clients send the KSEVENTDATA structure to the class driver to specify a notification method.</p>


## -syntax

````
typedef struct {
  ULONG NotificationType;
  union {
    struct {
      HANDLE    Event;
      ULONG_PTR Reserved[2];
    } EventHandle;
    struct {
      HANDLE Semaphore;
      ULONG  Reserved;
      LONG   Adjustment;
    } SemaphoreHandle;
    struct {
      PVOID    Unused;
      LONG_PTR Alignment[2];
    } Alignment;
  };
} KSEVENTDATA, *PKSEVENTDATA;
````


## -struct-fields
<dl>

### -field <b>NotificationType</b>

<dd>
<p>Contains flags indicating what type of notification should be performed. The following table lists all the possible values for the NotificationType member.</p>
<table>
<tr>
<th>NotificationType Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>KSEVENTF_EVENT_HANDLE</p>
</td>
<td>
<p>Indicates that a Win32 synchronization or notification object handle is being passed. The KSEVENTDATA.EventHandle.Event element contains the handle.</p>
</td>
</tr>
<tr>
<td>
<p>KSEVENTF_SEMAPHORE_HANDLE</p>
</td>
<td>
<p>Indicates that a Win32 semaphore handle is being passed. The KSEVENTDATA.SemaphoreHandle.Semaphore element contains the handle.</p>
</td>
</tr>
<tr>
<td>
<p>KSEVENTF_EVENT_OBJECT</p>
</td>
<td>
<p>Indicates that a pointer to a kernel synchronization or notification object is being passed. The KSEVENTDATA.EventObject.Event element contains a pointer to this object. This is available only to kernel-mode clients.</p>
</td>
</tr>
<tr>
<td>
<p>KSEVENTF_SEMAPHORE_OBJECT</p>
</td>
<td>
<p>Indicates that a pointer to a kernel semaphore object is being passed. The KSEVENTDATA.SemaphoreObject.Semaphore element contains a pointer to this object. This is available only to kernel-mode clients.</p>
</td>
</tr>
<tr>
<td>
<p>KSEVENTF_DPC</p>
</td>
<td>
<p>Indicates that a pointer to a kernel DPC structure is being passed. The KSEVENTDATA.Dpc.Dpc element contains a pointer to the DPC. This is available only to kernel-mode clients.</p>
</td>
</tr>
<tr>
<td>
<p>KSEVENTF_WORKITEM</p>
</td>
<td>
<p>Indicates that a pointer to a kernel work item structure is being passed. The KSEVENTDATA.WorkItem.WorkQueueItem contains a pointer to the work item. This is available only to kernel-mode clients.</p>
</td>
</tr>
<tr>
<td>
<p>KSEVENTF_KSWORKITEM</p>
</td>
<td>
<p>Indicates that a pointer to a kernel streaming work item structure is being passed. The KSEVENTDATA.KsWorkItem.WorkQueueItem contains a pointer to the work item, and is queued to a previously registered kernel streaming work item. This is available only to kernel-mode clients.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>EventHandle</b>

<dd>
<dl>

### -field <b>Event</b>

<dd>
<p>Contains a handle to a synchronization event when the KSEVENT_EVENT_HANDLE flag is set.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved and set to zero.</p>
</dd>
</dl>
</dd>

### -field <b>SemaphoreHandle</b>

<dd>
<dl>

### -field <b>Semaphore</b>

<dd>
<p>Contains a handle to a semaphore when the KSEVENT_SEMAPHORE_HANDLE flag is set.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved and set to zero.</p>
</dd>

### -field <b>Adjustment</b>

<dd>
<p>Contains the adjustment to the semaphore when it is released.</p>
</dd>
</dl>
</dd>

### -field <b>Alignment</b>

<dd>
<dl>

### -field <b>Unused</b>

<dd>
<p>Not used.</p>
</dd>

### -field <b>Alignment</b>

<dd>
<p>Reserved for internal use by AVStream. Minidrivers should not manipulate this member.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="NULL">KS Events</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551882">KDPC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557304">WORK_QUEUE_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566382">WORK_QUEUE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562678">KsIncrementCountedWorker</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566775">KsRegisterWorker</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSEVENTDATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
