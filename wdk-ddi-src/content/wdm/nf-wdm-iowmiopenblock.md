---
UID: NF.wdm.IoWMIOpenBlock
title: IoWMIOpenBlock function
author: windows-driver-content
description: The IoWMIOpenBlock routine opens the WMI data block object for the specified WMI class.
old-location: kernel\iowmiopenblock.htm
old-project: kernel
ms.assetid: c23d1861-59df-4bd4-a005-173ccac53049
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: IoWMIOpenBlock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Ntddk.h, Ntifs.h. The WMIGUID_XXX values are declared in Wmistr.h. To use them, include Wmistr.h.
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMIOpenBlock
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

# IoWMIOpenBlock function



## -description
The <b>IoWMIOpenBlock</b> routine opens the WMI data block object for the specified WMI class.



## -syntax

````
NTSTATUS IoWMIOpenBlock(
  _In_  GUID  *DataBlockGuid,
  _In_  ULONG DesiredAccess,
  _Out_ PVOID *DataBlockObject
);
````


## -parameters

### -param DataBlockGuid [in]

Specifies the GUID for WMI class.


### -param DesiredAccess [in]

Specifies the desired access rights to the data block object. The caller must have particular access rights to perform certain operations. 

The following is a description of each access right bit and the operations it allows:




### -param WMIGUID_EXECUTE

The data block object can be used to run WMI class methods. This flag must be set to use <a href="kernel.iowmiexecutemethod">IoWMIExecuteMethod</a> on the data block object. 


### -param WMIGUID_NOTIFICATION

The data block object can be used to register event notification callbacks. This flag must be set to use <a href="kernel.iowmisetnotificationcallback">IoWMISetNotificationCallback</a>, and can only be used for WMI event blocks. Callers that specify this flag must also specify the SYNCHRONIZE flag.


### -param WMIGUID_QUERY

The data block object can be used to query WMI class properties. This flag must be set to use any of the <b>IoWMIQuery<i>Xxx</i></b> routines on the data block object. 


### -param WMIGUID_SET

The data block object can be used to set WMI class properties. This flag must be set to use any of the <b>IoWMISet<i>Xxx</i></b> routines on the data block object. 

</dd>
</dl>

### -param DataBlockObject [out]

Pointer to a memory location where the routine returns a pointer to the data block object.


## -returns
Returns STATUS_SUCCESS on success, or the appropriate NTSTATUS error code on failure.


## -remarks
The caller uses <b>IoWMIOpenBlock</b> to create a data block object for the specified WMI class GUID. Subsequently, the caller can use the data block object to read or write WMI class properties, run WMI class methods, and register callbacks for WMI events.

Use the <b>IoWMIQuery<i>Xxx</i></b> and <b>IoWMISet<i>Xxx</i></b> routines to read and write WMI class properties. Use <a href="kernel.iowmiexecutemethod">IoWMIExecuteMethod</a> to run WMI class methods, and use <a href="kernel.iowmisetnotificationcallback">IoWMISetNotificationCallback</a> to register a WMI event notification callback.

Use <a href="kernel.obdereferenceobject">ObDereferenceObject</a> to close the data block object once it is no longer needed.


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
Available in Windows XP and later versions of the Windows operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (Include Wdm.h, Ntddk.h, or Ntifs.h. The WMIGUID_XXX values are declared in Wmistr.h. To use them, include Wmistr.h.)</dt>
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
<a href="kernel.iowmiexecutemethod">IoWMIExecuteMethod</a>
</dt>
<dt>
<a href="kernel.iowmiqueryalldata">IoWMIQueryAllData</a>
</dt>
<dt>
<a href="kernel.iowmiqueryalldatamultiple">IoWMIQueryAllDataMultiple</a>
</dt>
<dt>
<a href="kernel.iowmiquerysingleinstance">IoWMIQuerySingleInstance</a>
</dt>
<dt>
<a href="kernel.iowmiquerysingleinstancemultiple">IoWMIQuerySingleInstanceMultiple</a>
</dt>
<dt>
<a href="kernel.iowmisetnotificationcallback">IoWMISetNotificationCallback</a>
</dt>
<dt>
<a href="kernel.iowmisetsingleinstance">IoWMISetSingleInstance</a>
</dt>
<dt>
<a href="kernel.iowmisetsingleitem">IoWMISetSingleItem</a>
</dt>
<dt>
<a href="kernel.zwclose">ZwClose</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIOpenBlock routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

