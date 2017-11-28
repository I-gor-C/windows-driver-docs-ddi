---
UID: NC.ntddk.PLOAD_IMAGE_NOTIFY_ROUTINE
title: PLOAD_IMAGE_NOTIFY_ROUTINE
author: windows-driver-content
description: Called by the operating system to notify the driver when a driver image or a user image (for example, a DLL or EXE) is mapped into virtual memory.
old-location: kernel\pload_image_notify_routine.htm
old-project: kernel
ms.assetid: 613962D6-DF27-4AAE-BD8F-6BC0A538D7F8
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetLoadImageNotifyRoutine
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
req.iface: 
---

# PLOAD_IMAGE_NOTIFY_ROUTINE callback



## -description
<p>Called by the operating system to notify the driver when a driver image or a user image (for example, a DLL or EXE) is mapped into virtual memory. </p>


## -prototype

````
PLOAD_IMAGE_NOTIFY_ROUTINE SetLoadImageNotifyRoutine;

void SetLoadImageNotifyRoutine(
  _In_opt_ PUNICODE_STRING FullImageName,
  _In_     HANDLE          ProcessId,
  _In_     PIMAGE_INFO     ImageInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>FullImageName</i> [in, optional]

<dd>
<p>A pointer to a buffered Unicode string that identifies the executable image file. (The <i>FullImageName</i> parameter can be <b>NULL</b> in cases in which the operating system is unable to obtain the full name of the image at process creation time.) </p>
</dd>

### -param <i>ProcessId</i> [in]

<dd>
<p>The process ID of the process in which the image has been mapped, but this handle is zero if the newly loaded image is a driver.</p>
</dd>

### -param <i>ImageInfo</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt764083">IMAGE_INFO</a> structure that contains image information. See Remarks.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Highest-level system-profiling drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559957">PsSetLoadImageNotifyRoutine</a> to set up their load-image notify routine.</p>

<p>The operating system does not call load-image notify routines when sections created with the SEC_IMAGE_NO_EXECUTE attribute are mapped to virtual memory.</p>

<p>In Windows 7, Windows Server 2008 R2, and earlier versions of Windows, the operating system holds an internal system lock during calls to load-image notify routines for images loaded in user process address space (user space). To avoid deadlocks, load-image notify routines must not call system routines that map, allocate, query, free, or perform other operations on user-space virtual memory.</p>

<p>A driver must remove any callbacks it registers before it unloads. You can remove the callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559949">PsRemoveLoadImageNotifyRoutine</a> routine.</p>

<p>When the main executable image for a newly created process is loaded, the load-image notify routine runs in the context of the new process. The operating system calls the driver's load-image notify routine at PASSIVE_LEVEL inside a critical region with <a href="https://msdn.microsoft.com/74ed953c-1b2a-40b9-9df3-16869b198b38">normal kernel APCs</a> always disabled and sometimes with both kernel and special APCs disabled.</p>

<p>
        When the load-image notify routine is called, the input <i>FullImageName</i> points to a buffered Unicode string that identifies the executable image file. (The <i>FullImageName</i> parameter can be <b>NULL</b> in cases in which the operating system is unable to obtain the full name of the image at process creation time.) The <i>ProcessId</i> handle identifies the process in which the image has been mapped, but this handle is zero if the newly loaded image is a driver. To see the format of the buffered data at <i>ImageInfo</i>, see  <a href="https://msdn.microsoft.com/library/windows/hardware/mt764083">IMAGE_INFO</a>. If the <b>ExtendedInfoPresent</b> flag is set in the <b>IMAGE_INFO</b> structure, the information is part of a larger, extended version of the image information structure, <a href="https://msdn.microsoft.com/library/windows/hardware/mt764084">IMAGE_INFO_EX</a>.</p>

<p>Highest-level system-profiling drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559957">PsSetLoadImageNotifyRoutine</a> to set up their load-image notify routine.</p>

<p>The operating system does not call load-image notify routines when sections created with the SEC_IMAGE_NO_EXECUTE attribute are mapped to virtual memory.</p>

<p>In Windows 7, Windows Server 2008 R2, and earlier versions of Windows, the operating system holds an internal system lock during calls to load-image notify routines for images loaded in user process address space (user space). To avoid deadlocks, load-image notify routines must not call system routines that map, allocate, query, free, or perform other operations on user-space virtual memory.</p>

<p>A driver must remove any callbacks it registers before it unloads. You can remove the callback by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559949">PsRemoveLoadImageNotifyRoutine</a> routine.</p>

<p>When the main executable image for a newly created process is loaded, the load-image notify routine runs in the context of the new process. The operating system calls the driver's load-image notify routine at PASSIVE_LEVEL inside a critical region with <a href="https://msdn.microsoft.com/74ed953c-1b2a-40b9-9df3-16869b198b38">normal kernel APCs</a> always disabled and sometimes with both kernel and special APCs disabled.</p>

<p>
        When the load-image notify routine is called, the input <i>FullImageName</i> points to a buffered Unicode string that identifies the executable image file. (The <i>FullImageName</i> parameter can be <b>NULL</b> in cases in which the operating system is unable to obtain the full name of the image at process creation time.) The <i>ProcessId</i> handle identifies the process in which the image has been mapped, but this handle is zero if the newly loaded image is a driver. To see the format of the buffered data at <i>ImageInfo</i>, see  <a href="https://msdn.microsoft.com/library/windows/hardware/mt764083">IMAGE_INFO</a>. If the <b>ExtendedInfoPresent</b> flag is set in the <b>IMAGE_INFO</b> structure, the information is part of a larger, extended version of the image information structure, <a href="https://msdn.microsoft.com/library/windows/hardware/mt764084">IMAGE_INFO_EX</a>.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559957">PsSetLoadImageNotifyRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt764083">IMAGE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt764084">IMAGE_INFO_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PLOAD_IMAGE_NOTIFY_ROUTINE callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
