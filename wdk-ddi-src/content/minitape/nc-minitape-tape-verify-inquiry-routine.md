---
UID: NC.minitape.TAPE_VERIFY_INQUIRY_ROUTINE
title: TAPE_VERIFY_INQUIRY_ROUTINE
author: windows-driver-content
description: TapeMiniVerifyInquiry determines whether the tape miniclass driver recognizes and supports a given device. This routine is required.
old-location: storage\tapeminiverifyinquiry.htm
old-project: storage
ms.assetid: ed216b13-546a-4d0c-82db-79c175912556
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PROCESSOR_NUMBER, PROCESSOR_NUMBER, *PPROCESSOR_NUMBER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: minitape.h
req.include-header: Minitape.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TapeMiniVerifyInquiry
req.alt-loc: minitape.h
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
req.iface: 
---

# TAPE_VERIFY_INQUIRY_ROUTINE callback



## -description
<p><i>TapeMiniVerifyInquiry</i> determines whether the tape miniclass driver recognizes and supports a given device. This routine is required.</p>


## -prototype

````
TAPE_VERIFY_INQUIRY_ROUTINE TapeMiniVerifyInquiry;

BOOLEAN TapeMiniVerifyInquiry(
  _In_ PINQUIRYDATA            InquiryData,
  _In_ PMODE_CAPABILITIES_PAGE ModeCapabilitiesPage
)
{ ... }
````


## -parameters
<dl>

### -param <i>InquiryData</i> [in]

<dd>
<p>Pointer to SCSI inquiry data for the device.</p>
</dd>

### -param <i>ModeCapabilitiesPage</i> [in]

<dd>
<p>Pointer to a MODE_CAPABILITIES_PAGE structure that contains low-level information about the device. The format of this structure is defined by the QIC 157 standard and is subject to change. The pointer is <b>NULL</b> if the tape device does not support a mode capabilities page. </p>
</dd>
</dl>

## -returns
<p><i>TapeMiniVerifyInquiry</i> returns <b>TRUE</b> if the miniclass driver supports the device.</p>

## -remarks
<p><i>TapeMiniVerifyInquiry</i> examines the <i>InquiryData</i>, particularly the <b>VendorId</b> and <b>ProductId</b> members, to determine whether the tape miniclass driver supports the tape device. <i>TapeMiniVerifyInquiry</i> uses <a href="..\minitape\nf-minitape-tapeclasscomparememory.md">TapeClassCompareMemory</a> to compare ID strings against values the tape miniclass driver supports.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Minitape.h (include Minitape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\minitape\nf-minitape-tapeclasscomparememory.md">TapeClassCompareMemory</a>
</dt>
<dt>
<a href="..\minitape\ne-minitape--tape-status.md">TAPE_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TapeMiniVerifyInquiry routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
