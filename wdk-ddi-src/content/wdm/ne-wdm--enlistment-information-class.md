---
UID: NE.wdm._ENLISTMENT_INFORMATION_CLASS
title: ENLISTMENT_INFORMATION_CLASS
author: windows-driver-content
description: The ENLISTMENT_INFORMATION_CLASS enumeration identifies the type of information that the ZwSetInformationEnlistment routine can set and that the ZwQueryInformationEnlistment routine can retrieve for an enlistment object.
old-location: kernel\enlistment_information_class.htm
old-project: kernel
ms.assetid: d031e032-66e3-4697-8db1-67655cfc223d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ENLISTMENT_INFORMATION_CLASS enumeration



## -description
<p>The <b>ENLISTMENT_INFORMATION_CLASS</b> enumeration identifies the type of information that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567094">ZwSetInformationEnlistment</a> routine can set and that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567051">ZwQueryInformationEnlistment</a> routine can retrieve for an <a href="https://msdn.microsoft.com/80e61475-4bb7-4eaa-b9f1-ff95eac9bc77">enlistment object</a>.</p>


## -syntax

````
typedef enum _ENLISTMENT_INFORMATION_CLASS { 
  EnlistmentBasicInformation     = 0,
  EnlistmentRecoveryInformation,
  EnlistmentCrmInformation
} ENLISTMENT_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field <a id="EnlistmentBasicInformation"></a><a id="enlistmentbasicinformation"></a><a id="ENLISTMENTBASICINFORMATION"></a><b>EnlistmentBasicInformation</b>

<dd>
<p>Information about an enlistment object is stored in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544254">ENLISTMENT_BASIC_INFORMATION</a> structure.</p>
</dd>

### -field <a id="EnlistmentRecoveryInformation"></a><a id="enlistmentrecoveryinformation"></a><a id="ENLISTMENTRECOVERYINFORMATION"></a><b>EnlistmentRecoveryInformation</b>

<dd>
<p>A resource manager is setting or obtaining customized recovery information for an enlistment. To learn more about recovery information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567094">ZwSetInformationEnlistment</a>.</p>
</dd>

### -field <a id="EnlistmentCrmInformation"></a><a id="enlistmentcrminformation"></a><a id="ENLISTMENTCRMINFORMATION"></a><b>EnlistmentCrmInformation</b>

<dd>
<p>Information about an enlistment object is stored in an <b>ENLISTMENT_CRM_INFORMATION</b> structure.</p>
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
<p>Available starting with Windows Vista.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544254">ENLISTMENT_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567051">ZwQueryInformationEnlistment</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567094">ZwSetInformationEnlistment</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ENLISTMENT_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
