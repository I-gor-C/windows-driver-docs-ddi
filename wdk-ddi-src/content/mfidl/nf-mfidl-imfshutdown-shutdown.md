---
UID: NF:mfidl.IMFShutdown.Shutdown
title: IMFShutdown::Shutdown method
author: windows-driver-content
description: A print monitor's Shutdown function performs the tasks required to delete a monitor instance.
old-location: print\shutdown.htm
old-project: print
ms.assetid: 2b491920-299d-4ec9-a7a6-aa02f76cb67f
ms.author: windowsdriverdev
ms.date: 1/8/2018
ms.keywords: IMFShutdown, IMFShutdown::Shutdown, Shutdown
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: mfidl.h
req.include-header: Mfidl.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnShutdown
req.alt-loc: mfidl.h
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
req.typenames: MF_TRANSFER_VIDEO_FRAME_FLAGS
---

# IMFShutdown::Shutdown method



## -description
A print monitor's <code>Shutdown</code> function performs the tasks required to delete a monitor instance.



## -syntax

````
VOID WINAPI pfnShutdown(
  [in] HANDLE hMonitor
);
````


## -parameters

### -param hMonitor [in]

Caller supplied monitor instance handle. This is the handle returned by the monitor's <a href="..\winsplp\nf-winsplp-initializeprintmonitor2.md">InitializePrintMonitor2</a> function.


## -returns
<dl>
<dt><b>None</b></dt>
</dl> 


## -remarks

<a href="https://msdn.microsoft.com/26ba1c22-390a-4187-b67a-3f3497964f8e">Language monitors</a> and port monitor server DLLs are required to define a <code>Shutdown</code> function and include the function's address in a <a href="..\winsplp\ns-winsplp-_monitor2.md">MONITOR2</a> structure.

The function must return quickly. If multiple threads need to be terminated, they should just be marked for removal. Thread termination can occur after the function returns.

The <code>Shutdown</code> function should mark the following information as no longer valid:

The spooler handle received in the <a href="..\winsplp\ns-winsplp-_monitorinit.md">MONITORINIT</a> structure

The registry function pointers received in the <a href="..\winsplp\ns-winsplp-_monitorreg.md">MONITORREG</a> structure


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Mfidl.h (include Mfidl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winsplp\nf-winsplp-initializeprintmonitor2.md">InitializePrintMonitor2</a>
</dt>
<dt>
<a href="..\winsplp\ns-winsplp-_monitorinit.md">MONITORINIT</a>
</dt>
<dt>
<a href="..\winsplp\ns-winsplp-_monitorreg.md">MONITORREG</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20pfnShutdown method%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

