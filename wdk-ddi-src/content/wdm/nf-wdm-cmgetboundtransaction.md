---
UID: NF.wdm.CmGetBoundTransaction
title: CmGetBoundTransaction function
author: windows-driver-content
description: The CmGetBoundTransaction routine returns a pointer to the transaction object that represents the transaction, if any, that is associated with a specified registry key object.
old-location: kernel\cmgetboundtransaction.htm
old-project: kernel
ms.assetid: f38a5ad6-6816-4b27-98ea-51ac1453d90f
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: CmGetBoundTransaction
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CmGetBoundTransaction
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
req.irql: <= APC_LEVEL
req.product: Windows 10 or later.
---

# CmGetBoundTransaction function



## -description
The <b>CmGetBoundTransaction</b> routine returns a pointer to the transaction object that represents the <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">transaction</a>, if any, that is associated with a specified registry key object. 



## -syntax

````
PVOID CmGetBoundTransaction(
  _In_ PLARGE_INTEGER Cookie,
  _In_ PVOID          Object
);
````


## -parameters

### -param Cookie [in]

The cookie value that the driver previously obtain by calling <a href="kernel.cmregistercallback">CmRegisterCallback</a> or <a href="kernel.cmregistercallbackex">CmRegisterCallbackEx</a>. 


### -param Object [in]

The pointer value that the driver's <a href="kernel.registrycallback">RegistryCallback</a> callback routine received in one of the <b>REG_<i>XXX</i>_KEY_INFORMATION</b> structures. 


## -returns
<b>CmGetBoundTransaction</b> returns a pointer to a transaction object, if the key object that the <i>Object</i> parameter specifies is associated with a transaction. Otherwise, the routine returns <b>NULL</b>. 


## -remarks
The <b>CmGetBoundTransaction</b> routine is available on Windows Vista and later versions of Windows.

For more information about <b>CmGetBoundTransaction</b> and filtering registry operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.

For more information about transactions, see <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">Kernel Transaction Manager Design Guide</a>.


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
Available in Windows Vista and later versions of Windows.

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
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.cmregistercallback">CmRegisterCallback</a>
</dt>
<dt>
<a href="kernel.cmregistercallbackex">CmRegisterCallbackEx</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CmGetBoundTransaction routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

