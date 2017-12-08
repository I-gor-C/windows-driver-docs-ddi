---
UID: NF.wdm.ExInitializeSetTimerParameters
title: ExInitializeSetTimerParameters function
author: windows-driver-content
description: The ExInitializeSetTimerParameters routine initializes an EXT_SET_PARAMETERS structure.
old-location: kernel\exinitializesettimerparameters.htm
old-project: kernel
ms.assetid: 43A07E6E-C69F-4D6C-9B9C-EB7FFDF7651E
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: ExInitializeSetTimerParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExInitializeSetTimerParameters
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
req.irql: Any level.
req.product: Windows 10 or later.
---

# ExInitializeSetTimerParameters function



## -description
The <b>ExInitializeSetTimerParameters</b> routine initializes an <a href="kernel.ext_set_parameters">EXT_SET_PARAMETERS</a> structure.


## -syntax

````
VOID ExInitializeSetTimerParameters(
  _Out_ PEXT_SET_PARAMETERS Parameters
);
````


## -parameters

### -param Parameters [out]

A pointer to the <b>EXT_SET_PARAMETER</b> structure that is to be initialized.

## -returns
None.

## -remarks
Your driver must call <b>ExInitializeSetTimerParameters</b> to initialize an <b>EXT_SET_PARAMETERS</b> structure before the driver passes this structure to the <a href="kernel.exsettimer">ExSetTimer</a> routine. For more information about the member values that <b>ExInitializeSetTimerParameters</b> writes to the members of this structure, see <a href="kernel.ext_set_parameters">EXT_SET_PARAMETERS</a>.

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
Version
</th>
<td width="70%">
Available starting with Windows 8.1.
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
IRQL
</th>
<td width="70%">
Any level.
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exsettimer">ExSetTimer</a>
</dt>
<dt>
<a href="kernel.ext_set_parameters">EXT_SET_PARAMETERS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExInitializeSetTimerParameters routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
