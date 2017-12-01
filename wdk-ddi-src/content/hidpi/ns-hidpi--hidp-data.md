---
UID: NS.hidpi._HIDP_DATA
title: HIDP_DATA
author: windows-driver-content
description: The HIDP_DATA structure contains information about a HID control's data index and value in a HID report.
old-location: hid\hidp_data.htm
old-project: hid
ms.assetid: f48bbf84-027f-4579-b83c-7dfb1cbe6b65
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDP_DATA, HIDP_DATA, *PHIDP_DATA
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
req.alt-api: HIDP_DATA
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

# HIDP_DATA structure



## -description
<p>The HIDP_DATA structure contains information about a HID control's <a href="https://msdn.microsoft.com/84577544-515a-4fdc-86e5-518182c6c461">data index</a> and value in a HID report.</p>


## -syntax

````
typedef struct _HIDP_DATA {
  USHORT DataIndex;
  USHORT Reserved;
  union {
    ULONG   RawValue;
    BOOLEAN On;
  };
} HIDP_DATA, *PHIDP_DATA;
````


## -struct-fields
<dl>

### -field <b>DataIndex</b>

<dd>
<p>Specifies the data index of a control.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for internal system use only.</p>
</dd>

### -field <b>RawValue</b>

<dd>
<p>Contains the binary data extracted from a report if the control is a value.</p>
</dd>

### -field <b>On</b>

<dd>
<p>Specifies, if <b>TRUE</b> and the control is a button, that the button is set to ON (1). Otherwise, if <b>On</b> is <b>FALSE</b> and the control is a button, the button is set to OFF (zero).</p>
</dd>
</dl>

## -remarks
<p>See <a href="NULL">Extracting and Setting Control Data by Data Indices</a>.</p>

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
<a href="..\hidpi\nf-hidpi-hidp-getdata.md">HidP_GetData</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-setdata.md">HidP_SetData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_DATA structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
