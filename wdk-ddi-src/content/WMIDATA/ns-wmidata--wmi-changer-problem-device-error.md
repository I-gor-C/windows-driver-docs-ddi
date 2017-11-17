---
UID: NS.wmidata._WMI_CHANGER_PROBLEM_DEVICE_ERROR
title: WMI_CHANGER_PROBLEM_DEVICE_ERROR
author: windows-driver-content
description: When the ChangerPerformDiagnostics routine performs diagnostic tests on a changer device it returns the results in a WMI_CHANGER_PROBLEM_DEVICE_ERROR structure.
old-location: storage\wmi_changer_problem_device_error.htm
ms.assetid: c2c0f2eb-cb35-4f23-beb6-7f0eaeda845a
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: wmidata.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WMI_CHANGER_PROBLEM_DEVICE_ERROR
req.alt-loc: wmidata.h
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
ms.keywords: WMI_CHANGER_PROBLEM_DEVICE_ERROR, WMI_CHANGER_PROBLEM_DEVICE_ERROR, *PWMI_CHANGER_PROBLEM_DEVICE_ERROR
req.iface: 
req.product: Windows 10 or later.
---

# WMI_CHANGER_PROBLEM_DEVICE_ERROR structure



## -description
<p>When the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a> routine performs diagnostic tests on a changer device it returns the results in a WMI_CHANGER_PROBLEM_DEVICE_ERROR structure. </p>


## -syntax

````
typedef struct _WMI_CHANGER_PROBLEM_DEVICE_ERROR {
  ULONG ChangerProblemType;
} WMI_CHANGER_PROBLEM_DEVICE_ERROR, *PWMI_CHANGER_PROBLEM_DEVICE_ERROR;
````


## -struct-fields
<dl>

### -field <b>ChangerProblemType</b>

<dd>
<p>Contains one of the enumeration values defined for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551453">CHANGER_DEVICE_PROBLEM_TYPE</a> enumeration data type. The minidriver sets <b>ChangerProblemType</b> to the appropriate enumerator value. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wmidata.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551453">CHANGER_DEVICE_PROBLEM_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20WMI_CHANGER_PROBLEM_DEVICE_ERROR structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
