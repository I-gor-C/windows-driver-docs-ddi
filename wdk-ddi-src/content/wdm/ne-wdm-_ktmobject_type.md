---
UID : NE:wdm._KTMOBJECT_TYPE
title : _KTMOBJECT_TYPE
author : windows-driver-content
description : The KTMOBJECT_TYPE enumeration identifies the types of objects that KTM supports.
old-location : kernel\ktmobject_type.htm
old-project : kernel
ms.assetid : 0ace1cdf-0a15-48bb-9444-c947239e453e
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _KTMOBJECT_TYPE, *PKTMOBJECT_TYPE, KTMOBJECT_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later operating system versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KTMOBJECT_TYPE
req.alt-loc : Wdm.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PKTMOBJECT_TYPE, KTMOBJECT_TYPE"
req.product : Windows 10 or later.
---

# _KTMOBJECT_TYPE Enumeration
The <b>KTMOBJECT_TYPE</b> enumeration identifies the types of objects that KTM supports.

## Syntax
````
typedef enum _KTMOBJECT_TYPE { 
  KTMOBJECT_TRANSACTION          = 0,
  KTMOBJECT_TRANSACTION_MANAGER  = 1,
  KTMOBJECT_RESOURCE_MANAGER     = 2,
  KTMOBJECT_ENLISTMENT           = 3,
  KTMOBJECT_INVALID              = 4
} KTMOBJECT_TYPE, *PKTMOBJECT_TYPE;
````

## Constants

<table>

<tr>
<td>KTMOBJECT_ENLISTMENT</td>
<td>KTM enlistment objects.</td>
</tr>

<tr>
<td>KTMOBJECT_INVALID</td>
<td>Invalid object type.</td>
</tr>

<tr>
<td>KTMOBJECT_RESOURCE_MANAGER</td>
<td>KTM resource manager objects.</td>
</tr>

<tr>
<td>KTMOBJECT_TRANSACTION</td>
<td>KTM transaction objects.</td>
</tr>

<tr>
<td>KTMOBJECT_TRANSACTION_MANAGER</td>
<td>KTM transaction manager objects.</td>
</tr>
</table>

## Remarks

The <b>KTMOBJECT_TYPE</b> enumeration is used with the <a href="..\wdm\nf-wdm-zwenumeratetransactionobject.md">ZwEnumerateTransactionObject</a> routine.

For more information about KTM objects, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554272">KTM Objects</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<dl>
<dt>
<a href="..\wdm\nf-wdm-zwenumeratetransactionobject.md">ZwEnumerateTransactionObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KTMOBJECT_TYPE enumeration%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>