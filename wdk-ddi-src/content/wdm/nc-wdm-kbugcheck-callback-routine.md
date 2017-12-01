---
UID: NC.wdm.KBUGCHECK_CALLBACK_ROUTINE
title: KBUGCHECK_CALLBACK_ROUTINE
author: windows-driver-content
description: The BugCheckCallback routine is executed whenever the system issues a bug check.
old-location: kernel\bugcheckcallback.htm
old-project: kernel
ms.assetid: ecd777f0-bba2-4f14-9fa6-8f47ac83fe7f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BugCheckCallback
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at HIGH_LEVEL.
req.iface: 
req.product: Windows 10 or later.
---

# KBUGCHECK_CALLBACK_ROUTINE callback



## -description
<p>The <i>BugCheckCallback</i> routine is executed whenever the system issues a bug check.</p>


## -prototype

````
KBUGCHECK_CALLBACK_ROUTINE BugCheckCallback;

VOID BugCheckCallback(
  _In_ PVOID Buffer,
  _In_ ULONG Length
)
{ ... }
````


## -parameters
<dl>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the buffer that was specified when the callback was registered.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the length, in bytes, of the buffer that is pointed to by the <i>Buffer</i> parameter.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers can supply a <i>BugCheckCallback</i> that resets the device to a known state if the system issues a bug check.</p>

<p>Use <a href="..\wdm\nf-wdm-keregisterbugcheckcallback.md">KeRegisterBugCheckCallback</a> to register a <i>BugCheckCallback</i> routine. A driver can subsequently remove the callback by using the <a href="..\wdm\nf-wdm-kederegisterbugcheckcallback.md">KeDeregisterBugCheckCallback</a> routine. If the driver can be unloaded, it must remove any registered callbacks in its <a href="kernel.unload">Unload</a> routine.</p>

<p>A <i>BugCheckCallback</i> routine is strongly restricted in the actions it can take. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566401">Writing a Bug Check Callback Routine</a>. The routine <u>can</u> safely use the <b>READ_PORT_<i>XXX</i></b>, <b>READ_REGISTER_<i>XXX</i></b>, <b>WRITE_PORT_<i>XXX</i></b>, and <b>WRITE_REGISTER_<i>XXX</i></b> routines to interact with the device.</p>

<p>Drivers that require more sophisticated interaction with the system as it issues a bug check can instead implement <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a> or <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a> routines.</p>

<p>Note that beginning with the Windows XP SP1 and Windows Server 2003 operating systems, <i>BugCheckCallback</i> routines execute after the system crash dump file has already been written. (On earlier versions of Windows, the routines execute <u>before</u> the crash dump file is written.) Thus, any data that is stored in the buffer specified by the <i>Buffer</i> parameter will not appear in the crash dump file. Drivers that are required to write data to the crash dump file instead implement a <a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a> routine. (On earlier versions of Windows, the data written to <i>Buffer</i> does appear in the crash dump file.) </p>

<p>To define a <i>BugCheckCallback</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>BugCheckCallback</i> callback routine that is named <code>MyBugCheckCallback</code>, use the KBUGCHECK_CALLBACK_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The KBUGCHECK_CALLBACK_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the KBUGCHECK_CALLBACK_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at HIGH_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-kederegisterbugcheckcallback.md">KeDeregisterBugCheckCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keregisterbugcheckcallback.md">KeRegisterBugCheckCallback</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckDumpIoCallback</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BugCheckCallback routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
