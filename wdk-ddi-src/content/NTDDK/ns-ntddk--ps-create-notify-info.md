---
UID: NS.ntddk._PS_CREATE_NOTIFY_INFO
title: PS_CREATE_NOTIFY_INFO
author: windows-driver-content
description: The PS_CREATE_NOTIFY_INFO structure provides information about a newly created process.
old-location: kernel\ps_create_notify_info.htm
ms.assetid: 66fade6b-b1c1-477c-bd44-2809d02271f2
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PS_CREATE_NOTIFY_INFO
req.alt-loc: Ntddk.h
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
ms.keywords: PS_CREATE_NOTIFY_INFO, PS_CREATE_NOTIFY_INFO, *PPS_CREATE_NOTIFY_INFO
req.iface: 
---

# PS_CREATE_NOTIFY_INFO structure



## -description
<p>The <b>PS_CREATE_NOTIFY_INFO</b> structure provides information about a newly created process.</p>


## -syntax

````
typedef struct _PS_CREATE_NOTIFY_INFO {
  SIZE_T              Size;
  union {
    ULONG  Flags;
    struct {
      ULONG FileOpenNameAvailable  :1;
      ULONG IsSubsystemProcess   :1;
      ULONG Reserved  :30;
    };
  };
  HANDLE              ParentProcessId;
  CLIENT_ID           CreatingThreadId;
  struct _FILE_OBJECT  *FileObject;
  PCUNICODE_STRING    ImageFileName;
  PCUNICODE_STRING    CommandLine;
  NTSTATUS            CreationStatus;
} PS_CREATE_NOTIFY_INFO, *PPS_CREATE_NOTIFY_INFO;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure. The operating system uses this size to indicate the type of structure that it passes to <a href="kernel.createprocessnotifyex">CreateProcessNotifyEx</a>. Currently, this member is always <b>sizeof</b>(<b>PS_CREATE_NOTIFY_INFO</b>).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved. Use the <b>FileOpenNameAvailable</b> member instead. </p>
</dd>

### -field <b>FileOpenNameAvailable</b>

<dd>
<p>A Boolean value that specifies whether the <b>ImageFileName</b> member contains the exact file name that is used to open the process executable file.</p>
</dd>

### -field <b>IsSubsystemProcess </b>

<dd>
<p>A Boolean value that indicates the type of process subsystem is a subsystem other than Win32. </p>
<div class="alert"><b>Note</b>  <p class="note"><b>IsSubsystemProcess</b> is only populated for subsystem processes other than Win32 when a driver has registered through <a href="https://msdn.microsoft.com/library/windows/hardware/mt805891">PsSetCreateProcessNotifyRoutineEx2</a> with a type that allows for notifications from subsystem processes.  When <b>IsSubsystemProcess</b> is set, the <b>FileObject</b>, <b>ImageFileName</b>, and <b>CommandLine</b> may be NULL.  Drivers should use <b>ProcessSubsystemInformation</b> to query the subsystem type if needed. 
For more information, see <a href="base.ntqueryinformationprocess">NtQueryInformationProcess</a>.</p>
</div>
<div> </div>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>ParentProcessId</b>

<dd>
<p>The process ID of the parent process for the new process. Note that the parent process is not necessarily the same process as the process that created the new process. The new process can inherit certain properties of the parent process, such as handles or shared memory. (The process ID of the process creator is given by <b>CreatingThreadId</b>-&gt;<b>UniqueProcess</b>.)</p>
</dd>

### -field <b>CreatingThreadId</b>

<dd>
<p>The process ID and thread ID of the process and thread that created the new process. <b>CreatingThreadId</b>-&gt;<b>UniqueProcess</b> contains the process ID, and <b>CreatingThreadId</b>-&gt;<b>UniqueThread</b> contains the thread ID.</p>
</dd>

### -field <b>FileObject</b>

<dd>
<p>A pointer to the file object for the process executable file. </p>
<div class="alert"><b>Note</b>  <p class="note">If <b>IsSubsystemProcess</b> is TRUE, this value may be NULL. </p>
</div>
<div> </div>
</dd>

### -field <b>ImageFileName</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> string that holds the file name of the executable. If the <b>FileOpenNameAvailable</b> member is <b>TRUE</b>, the string specifies the exact file name that is used to open the executable file. If <b>FileOpenNameAvailable</b> is <b>FALSE</b>, the operating system might provide only a partial name.</p>
<div class="alert"><b>Note</b>  <p class="note">If <b>IsSubsystemProcess</b> is TRUE, this value maybe NULL. </p>
</div>
<div> </div>
</dd>

### -field <b>CommandLine</b>

<dd>
<p>A pointer to a <b>UNICODE_STRING</b> string that holds the command that is used to execute the process. If the command is not available, <b>CommandLine</b> is <b>NULL</b>.</p>
<div class="alert"><b>Note</b>  <p class="note">If <b>IsSubsystemProcess</b> is TRUE, this value maybe NULL. </p>
</div>
<div> </div>
</dd>

### -field <b>CreationStatus</b>

<dd>
<p>The NTSTATUS value to return for the process-creation operation. Drivers can change this value to an error code to prevent the process from being created.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.createprocessnotifyex">CreateProcessNotifyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559953">PsSetCreateProcessNotifyRoutineEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PS_CREATE_NOTIFY_INFO structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
