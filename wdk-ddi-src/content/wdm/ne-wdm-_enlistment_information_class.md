---
UID: NE.wdm._ENLISTMENT_INFORMATION_CLASS
title: _ENLISTMENT_INFORMATION_CLASS
author: windows-driver-content
description: The ENLISTMENT_INFORMATION_CLASS enumeration identifies the type of information that the ZwSetInformationEnlistment routine can set and that the ZwQueryInformationEnlistment routine can retrieve for an enlistment object.
old-location: kernel\enlistment_information_class.htm
old-project: kernel
ms.assetid: d031e032-66e3-4697-8db1-67655cfc223d
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _ENLISTMENT_INFORMATION_CLASS, ENLISTMENT_INFORMATION_CLASS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ENLISTMENT_INFORMATION_CLASS
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
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# _ENLISTMENT_INFORMATION_CLASS enumeration



## -description
The <b>ENLISTMENT_INFORMATION_CLASS</b> enumeration identifies the type of information that the <a href="kernel.zwsetinformationenlistment">ZwSetInformationEnlistment</a> routine can set and that the <a href="kernel.zwqueryinformationenlistment">ZwQueryInformationEnlistment</a> routine can retrieve for an <a href="https://msdn.microsoft.com/80e61475-4bb7-4eaa-b9f1-ff95eac9bc77">enlistment object</a>.



## -syntax

````
typedef enum _ENLISTMENT_INFORMATION_CLASS { 
  EnlistmentBasicInformation     = 0,
  EnlistmentRecoveryInformation,
  EnlistmentCrmInformation
} ENLISTMENT_INFORMATION_CLASS;
````


## -enum-fields

### -field EnlistmentBasicInformation

Information about an enlistment object is stored in an <a href="kernel.enlistment_basic_information">ENLISTMENT_BASIC_INFORMATION</a> structure.


### -field EnlistmentRecoveryInformation

A resource manager is setting or obtaining customized recovery information for an enlistment. To learn more about recovery information, see <a href="kernel.zwsetinformationenlistment">ZwSetInformationEnlistment</a>.


### -field EnlistmentCrmInformation

Information about an enlistment object is stored in an <b>ENLISTMENT_CRM_INFORMATION</b> structure.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows Vista.

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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.enlistment_basic_information">ENLISTMENT_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="kernel.zwqueryinformationenlistment">ZwQueryInformationEnlistment</a>
</dt>
<dt>
<a href="kernel.zwsetinformationenlistment">ZwSetInformationEnlistment</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ENLISTMENT_INFORMATION_CLASS enumeration%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

