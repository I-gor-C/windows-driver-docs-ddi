---
UID: NC.wdm.KBUGCHECK_REASON_CALLBACK_ROUTINE
title: KBUGCHECK_REASON_CALLBACK_ROUTINE
author: windows-driver-content
description: The BugCheckDumpIoCallback routine is executed each time the system writes data to a crash dump file.
old-location: kernel\bugcheckdumpiocallback.htm
old-project: kernel
ms.assetid: 72c216d9-87e3-4e33-8985-cc9b0e807bc7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Drivers can implement BugCheckDumpIoCallback routines starting with Windows XP SP1 and Windows Server 2003.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BugCheckDumpIoCallback
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

# KBUGCHECK_REASON_CALLBACK_ROUTINE callback



## -description
<p>The <i>BugCheckDumpIoCallback</i> routine is executed each time the system writes data to a crash dump file.</p>


## -prototype

````
KBUGCHECK_REASON_CALLBACK_ROUTINE BugCheckDumpIoCallback;

VOID BugCheckDumpIoCallback(
  _In_    KBUGCHECK_CALLBACK_REASON                Reason,
  _In_    struct _KBUGCHECK_REASON_CALLBACK_RECORD *Record,
  _Inout_ PVOID                                    ReasonSpecificData,
  _In_    ULONG                                    ReasonSpecificDataLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>Reason</i> [in]

<dd>
<p>Specifies the situation in which the callback is executed. For <i>BugCheckDumpIoCallback</i>, the value of this parameter is always <b>KbCallbackDumpIo</b>. <b>KbCallbackDumpIo</b> is a <a href="..\wdm\ne-wdm--kbugcheck-callback-reason.md">KBUGCHECK_CALLBACK_REASON</a> enumeration value.</p>
</dd>

### -param <i>Record</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551873">KBUGCHECK_REASON_CALLBACK_RECORD</a> structure that the driver passed when registering this callback.</p>
</dd>

### -param <i>ReasonSpecificData</i> [in, out]

<dd>
<p>Pointer to a <a href="..\wdm\ns-wdm--kbugcheck-dump-io.md">KBUGCHECK_DUMP_IO</a> structure that describes the current I/O operation.</p>
</dd>

### -param <i>ReasonSpecificDataLength</i> [in]

<dd>
<p>Specifies the size of the buffer  supplied by the <i>ReasonSpecificData</i> parameter. For <i>BugCheckDumpIoCallback</i>, the value of this parameter is always <b>sizeof</b>(<b>KBUGCHECK_DUMP_IO</b>).</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The driver's <i>BugCheckDumpIoCallback</i> routine is called each time data is written to the crash dump file. The system passes, in the <i>ReasonSpecificData</i> parameter, a description of the data being written. The <b>Buffer</b> member points to the current data, and the <b>BufferLength</b> member specifies its length. The <b>Type</b> member indicates the type of data currently being written, such as dump file header information, memory state, or data provided by a driver. For a description of the possible types of information, see <a href="..\wdm\ne-wdm--kbugcheck-dump-io-type.md">KBUGCHECK_DUMP_IO_TYPE</a>.</p>

<p>The system can write the crash dump file either sequentially, or out of order. If the system is writing the crash dump file sequentially, then the <b>Offset</b> member of <i>ReasonSpecificData</i> is -1; otherwise, <b>Offset</b> is set to the current offset, in bytes, in the crash dump file.</p>

<p>When the system writes the file sequentially, it calls each <i>BugCheckDumpIoCallback</i> routine one or more times when writing the header information (<b>Type</b> = <b>KbDumpIoHeader</b>), one or more times when writing the main body of the crash dump file (<b>Type</b> = <b>KbDumpIoBody</b>), and one or more times when writing the secondary dump data (<b>Type</b> = <b>KbDumpIoSecondaryDumpData</b>). Once the system has completed writing the crash dump file, it calls the callback with <b>Buffer</b> = <b>NULL</b>, <b>BufferLength</b> = 0, and <b>Type</b> = <b>KbDumpIoComplete</b>.</p>

<p>The main purpose of a <i>BugCheckDumpIoCallback</i> routine is to allow system crash dump data to be written to devices other than the disk. For example, a device that monitors system state can use the callback to report that the system has issued a bug check, and to provide a crash dump for analysis.</p>

<p>Use <a href="..\wdm\nf-wdm-keregisterbugcheckreasoncallback.md">KeRegisterBugCheckReasonCallback</a> to register a <i>BugCheckDumpIoCallback</i> routine. A driver can subsequently remove the callback by using the <a href="..\wdm\nf-wdm-kederegisterbugcheckreasoncallback.md">KeDeregisterBugCheckReasonCallback</a> routine. If the driver can be unloaded, it must remove any registered callbacks in its <a href="kernel.unload">Unload</a> routine.</p>

<p>A <i>BugCheckDumpIoCallback</i> routine is strongly restricted in the actions it can take. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566401">Writing a Bug Check Callback Routine</a>.</p>

<p>To define a <i>BugCheckDumpIoCallback</i> callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>BugCheckDumpIoCallback</i> callback routine that is named <code>MyBugCheckDumpIoCallback</code>, use the KBUGCHECK_REASON_CALLBACK_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The KBUGCHECK_REASON_CALLBACK_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the KBUGCHECK_REASON_CALLBACK_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Drivers can implement <i>BugCheckDumpIoCallback</i> routines starting with Windows XP SP1 and Windows Server 2003.</p>
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
<a href="..\wdm\ns-wdm--kbugcheck-dump-io.md">KBUGCHECK_DUMP_IO</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--kbugcheck-dump-io-type.md">KBUGCHECK_DUMP_IO_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551873">KBUGCHECK_REASON_CALLBACK_RECORD</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-kebugcheck.md">KeBugCheck</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kebugcheckex.md">KeBugCheckEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kederegisterbugcheckcallback.md">KeDeregisterBugCheckCallback</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keregisterbugcheckcallback.md">KeRegisterBugCheckCallback</a>
</dt>
<dt>
<a href="kernel.bugcheckcallback">BugCheckCallback</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-kbugcheck-reason-callback-routine.md">BugCheckSecondaryDumpDataCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KBUGCHECK_REASON_CALLBACK_ROUTINE routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
