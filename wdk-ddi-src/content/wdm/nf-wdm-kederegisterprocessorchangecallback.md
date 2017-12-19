---
UID: NF.wdm.KeDeregisterProcessorChangeCallback
title: KeDeregisterProcessorChangeCallback function
author: windows-driver-content
description: The KeDeregisterProcessorChangeCallback routine unregisters a callback function that was previously registered with the operating system by calling the KeRegisterProcessorChangeCallback routine.
old-location: kernel\kederegisterprocessorchangecallback.htm
old-project: kernel
ms.assetid: 69b0f360-dfe5-4e1f-bdcb-0f908ed129a7
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeDeregisterProcessorChangeCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Server 2008 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeDeregisterProcessorChangeCallback
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
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# KeDeregisterProcessorChangeCallback function



## -description
The <b>KeDeregisterProcessorChangeCallback</b> routine unregisters a callback function that was previously registered with the operating system by calling the <a href="kernel.keregisterprocessorchangecallback">KeRegisterProcessorChangeCallback</a> routine.



## -syntax

````
VOID KeDeregisterProcessorChangeCallback(
  _In_ PVOID CallbackHandle
);
````


## -parameters

### -param CallbackHandle [in]

The callback registration handle that was returned by the <a href="kernel.keregisterprocessorchangecallback">KeRegisterProcessorChangeCallback</a> routine when the callback function was registered with the operating system. 


## -returns
None


## -remarks
A device driver calls the <a href="kernel.keregisterprocessorchangecallback">KeRegisterProcessorChangeCallback</a> routine to register a callback function with the operating system so that the operating system will notify the driver when a new processor is added to the hardware partition. When the device driver no longer needs to receive notification when new processors are added to the hardware paritition, it calls the <b>KeDeregisterProcessorChangeCallback</b> routine to unregister the callback function. A callback function that has been registered for notification of processor changes must be unregistered before the device driver is unloaded from the operating system. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Server 2008 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keregisterprocessorchangecallback">KeRegisterProcessorChangeCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeDeregisterProcessorChangeCallback routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

