---
UID: NF.ntddk.KeBugCheck
title: KeBugCheck
author: windows-driver-content
description: The KeBugCheck routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run.
old-location: kernel\kebugcheck.htm
old-project: kernel
ms.assetid: 46337a5f-dc8a-42bc-a618-0d1440270f91
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeBugCheck
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeBugCheck
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
req.irql: Any level
req.iface: 
---

# KeBugCheck function



## -description
<p>The <b>KeBugCheck</b> routine brings down the system in a controlled manner when the caller discovers an unrecoverable inconsistency that would corrupt the system if the caller continued to run. </p>


## -syntax

````
VOID KeBugCheck(
  _In_ ULONG BugCheckCode
);
````


## -parameters
<dl>

### -param <i>BugCheckCode</i> [in]

<dd>
<p>Specifies a value that indicates the reason for the bug check. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A bug check is a system-detected error that causes an immediate, controlled shutdown of the system. Various kernel-mode components perform run-time consistency checking. When such a component discovers an unrecoverable inconsistency, it causes a bug check to be generated.</p>

<p>Whenever possible, all kernel-mode components should log an error and continue to run, rather than calling <b>KeBugCheck</b>. For example, if a driver is unable to allocate required resources, it should log an error so that the system continues to run; it must not generate a bug check.</p>

<p>A driver or other kernel-mode component should call this routine only in cases of a fatal, unrecoverable error that could corrupt the system itself.</p>

<p><b>KeBugCheck</b> can be useful in the early stages of developing a driver, or while it is undergoing testing. In these circumstances, the <i>BugCheckCode</i> passed to this routine should be distinct from those codes already in use by Windows or its drivers. For a list of these codes, see <a href="https://msdn.microsoft.com/DBA85578-97CF-4BD7-A67D-1C7AD2E9B2BB">Bug Check Codes</a>.</p>

<p>However, even during driver development, this routine is of only limited utility, since it results in a complete system shutdown. A more effective debugging method is to attach a kernel debugger to the system and then use routines that send messages to the debugger or break into the debugger. For further information, see <a href="NULL">Using Debugging Code in a Driver</a>.</p>

<p>When a bug check is unavoidable, most system components call <a href="..\wdm\nf-wdm-kebugcheckex.md">KeBugCheckEx</a>, which provides more information about the cause of such an inconsistency than <b>KeBugCheck</b>. </p>

## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioallocateerrorlogentry.md">IoAllocateErrorLogEntry</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-iowriteerrorlogentry.md">IoWriteErrorLogEntry</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kebugcheckex.md">KeBugCheckEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keregisterbugcheckcallback.md">KeRegisterBugCheckCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keregisterbugcheckreasoncallback.md">KeRegisterBugCheckReasonCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeBugCheck routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
