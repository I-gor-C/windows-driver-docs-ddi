---
UID: NF.wdm.EtwWriteEx
title: EtwWriteEx
author: windows-driver-content
description: The EtwWriteEx function is a tracing function for publishing events that support filtering in your kernel-mode driver code.
old-location: devtest\etwwriteex.htm
old-project: devtest
ms.assetid: E2EF929A-61EB-412B-B8E8-D51FD6944B1D
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: EtwWriteEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 7
req.target-min-winversvr: Windows Server 2008 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EtwWriteEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# EtwWriteEx function



## -description
<p>The <b>EtwWriteEx</b> function is a tracing function for publishing events that support filtering in your kernel-mode driver code. </p>


## -syntax

````
NTSTATUS EtwWriteEx(
  _In_     REGHANDLE              RegHandle,
  _In_     PCEVENT_DESCRIPTOR     EventDescriptor,
  _In_     ULONG64                Filter,
  _In_     ULONG                  Flags,
  _In_opt_ LPCGUID                ActivityId,
  _In_opt_ LPCGUID                RelatedActivityId,
  _In_     ULONG                  UserDataCount,
  _In_opt_ PEVENT_DATA_DESCRIPTOR UserData
);
````


## -parameters
<dl>

### -param <i>RegHandle</i> [in]

<dd>
<p>A pointer to the event provider registration handle, which is returned by the <a href="..\wdm\nf-wdm-etwregister.md">EtwRegister</a> function if the event provider registration is successful.</p>
</dd>

### -param <i>EventDescriptor</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/cfe84b3d-fed2-4624-9899-8451e5b39de0">EVENT_DESCRIPTOR</a> structure. </p>
</dd>

### -param <i>Filter</i> [in]

<dd>
<p>The instance identifiers that identify the session to which the event will not written. That is, the value is a mask of sessions which should be excluded from logging (filtered out). Use a bitwise OR to specify multiple identifiers. Set to zero if you do not support filters or if the event is being written to all sessions (no filters failed). For information on getting the identifier for a session, see the <i>FilterData</i> parameter of your <a href="devtest.etwenablecallback">EtwEnableCallback</a> callback.  </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Reserved.  Must be  zero (0). </p>
</dd>

### -param <i>ActivityId</i> [in, optional]

<dd>
<p>The identifier that indicates the activity associated with the event. The <i>ActivityID</i> provides a way to group related events and is used in end-to-end tracing.  If NULL, ETW gets the identifier from the thread local storage. For details on getting this identifier, see <a href="..\wdm\nf-wdm-etwactivityidcontrol.md">EtwActivityIdControl</a>.</p>
</dd>

### -param <i>RelatedActivityId</i> [in, optional]

<dd>
<p>Activity identifier from the previous component. Use this parameter to link your component's events to the previous component's events. To get the activity identifier that was set for the previous component, see the descriptions for the <i>ControlCode</i> parameter of the <a href="..\wdm\nf-wdm-etwactivityidcontrol.md">EtwActivityIdControl</a> function.</p>
</dd>

### -param <i>UserDataCount</i> [in]

<dd>
<p>Number of EVENT_DATA_DESCRIPTOR structures in <i>UserData</i>. The maximum number is 128.</p>
</dd>

### -param <i>UserData</i> [in, optional]

<dd>
<p>A pointer to the array of EVENT_DATA_DESCRIPTOR structures. Set this parameter to NULL if <i>UserDataCount</i> is zero. The data must be in the order specified in the manifest.</p>
</dd>
</dl>

## -returns
<p>Returns ERROR_SUCCESS if successful or one of the following values on error.</p>

## -remarks
<p>The <b>EtwWriteEx</b> function is the kernel-mode equivalent of the user-mode <a href="etw.eventwriteex">EventWriteEx</a> function. Event data written with this function requires a manifest. The manifest is embedded in the provider, so the provider must be available for a consumer to consume the data. To ensure that there is a consumer for the event you are publishing, you can precede the call to <b>EtwWrite</b> with a call to <a href="..\wdm\nf-wdm-etweventenabled.md">EtwEventEnabled</a> or <a href="..\wdm\nf-wdm-etwproviderenabled.md">EtwProviderEnabled</a>. </p>

<p>Use the <i>ActivityId</i> and <i>RelatedActivityId</i> parameters when you want to relate events in different components in an end-to-end tracing scenario. For example, components A, B, and C perform work on a related activity and want to link their events so that a consumer can consume all the events related to that activity. </p>

<p>You can call <b>EtwWriteEx</b> at any IRQL. However, when IRQL is greater than APC_LEVEL, any data passed to the <b>EtwWrite</b>, <b>EtwWriteEx</b>, <b>EtwWriteString</b>, <b>EtwWriteTransfer</b> functions must not be pageable. That is, any kernel-mode routine that is running at IRQL greater than APC_LEVEL cannot access pageable memory.  Data passed to the <b>EtwWrite</b>, <b>EtwWriteEx</b>, <b>EtwWriteString</b>,  and <b>EtwWriteTransfer</b> functions must reside in system-space memory, regardless of what the IRQL is.</p>

<p></p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="etw.eventwriteex">EventWriteEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-etwwrite.md">EtwWrite</a>
</dt>
<dt>
<a href="etw.eventwrite_func">EventWrite</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [devtest\devtest]:%20EtwWriteEx function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
