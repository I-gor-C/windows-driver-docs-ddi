---
UID: NS.hidpi._USAGE_AND_PAGE
title: USAGE_AND_PAGE
author: windows-driver-content
description: The USAGE_AND_PAGE structure specifies the usage page and usage ID of a HID control.
old-location: hid\usage_and_page.htm
old-project: hid
ms.assetid: 48716117-c539-4436-a81f-4b05c9a8cb7d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USAGE_AND_PAGE, USAGE_AND_PAGE, *PUSAGE_AND_PAGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidpi.h
req.include-header: Hidpi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USAGE_AND_PAGE
req.alt-loc: hidpi.h
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
req.iface: 
---

# USAGE_AND_PAGE structure



## -description
<p>The USAGE_AND_PAGE structure specifies the <a href="hid.hid_usages#usage_page#usage_page">usage page</a> and <a href="hid.hid_usages#usage_id#usage_id">usage ID</a> of a HID control.</p>


## -syntax

````
typedef struct _USAGE_AND_PAGE {
  USAGE Usage;
  USAGE UsagePage;
} USAGE_AND_PAGE, *PUSAGE_AND_PAGE;
````


## -struct-fields
<dl>

### -field Usage

<dd>
<p>Specifies a usage ID within the usage page specified by <b>UsagePage</b>.</p>
</dd>

### -field UsagePage

<dd>
<p>Specifies a usage page.</p>
</dd>
</dl>

## -remarks
<p>The<b> HidP_IsSameUsageAndPage</b> macro determines if two <a href="hid.hid_usages#extended_usage#extended_usage">extended usages</a>, represented by <b>USAGE_AND_PAGE</b> structures, are equal.</p>

<p>
<pre class="syntax">BOOLEAN HidP_IsSameUsageAndPage(
   USAGE_AND_PAGE u1,
   USAGE_AND_PAGE u2
);
</pre>
</p>

<p><i>u1</i></p>

<p><b>USAGE_AND_PAGE</b></p>

<p>Specifies an extended usage</p>

<p><i>u2</i></p>

<p><b>Return Value</b></p>

<p><b>BOOLEAN</b></p>

<p><b>HidP_IsSameUsageAndPage</b> returns one of the following status values:</p>

<p><b>TRUE</b></p>

<p>Usage <i>u1</i> is the same as usage <i>u2</i>.</p>

<p><b>FALSE</b></p>

<p>Usage <i>u1</i> is different than usage <i>u2</i>.</p>

<p>As defined by the USB HID standard, an extended usage is a 32-bit unsigned value. The high-order 16 bits specify the <a href="hid.hid_usages#usage_page#usage_page">usage page</a>, and lower-order 16 bits specify the <a href="hid.hid_usages#usage_id#usage_id">usage ID</a>.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID Collections</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidpi.h (include Hidpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539712">HidP_GetButtonsEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20USAGE_AND_PAGE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
