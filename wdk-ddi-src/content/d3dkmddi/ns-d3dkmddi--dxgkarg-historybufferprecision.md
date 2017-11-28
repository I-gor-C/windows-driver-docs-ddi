---
UID: NS.d3dkmddi._DXGKARG_HISTORYBUFFERPRECISION
title: DXGKARG_HISTORYBUFFERPRECISION
author: windows-driver-content
description: Indicates info about the precision of history buffer data used by the display miniport driver.
old-location: display\dxgkarg_historybufferprecision.htm
old-project: display
ms.assetid: D55A8B5A-4133-4CE8-AD08-F551A3AEA42C
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_HISTORYBUFFERPRECISION, DXGKARG_HISTORYBUFFERPRECISION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_HISTORYBUFFERPRECISION
req.alt-loc: D3dkmddi.h
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

# DXGKARG_HISTORYBUFFERPRECISION structure



## -description
<p>Indicates info about the precision of history buffer data used by the display miniport driver.</p>


## -syntax

````
typedef struct _DXGKARG_HISTORYBUFFERPRECISION {
  UINT32 PrecisionBits;
} DXGKARG_HISTORYBUFFERPRECISION;
````


## -struct-fields
<dl>

### -field <b>PrecisionBits</b>

<dd>
<p>The number of valid bits that are used in each time stamp. This number doesn't include bits used for junk values.</p>
<p>This precision value has three valid ranges:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>No bits contain useful data, and the  DirectX graphics kernel subsystem will call the <a href="display.dxgkddiformathistorybuffer">DxgkDdiFormatHistoryBuffer</a> function to provide valid data to output to the Event Tracing for Windows (ETW) facility. When the driver processes this call, it sets a new precision value as the output parameter of the function.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 32

</dl>
</td>
<td width="60%">
<p>The driver should log 32-bit time stamps using the full 32 bits of precision.</p>
<p></p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 33–64

</dl>
</td>
<td width="60%">
<p>The driver should log 64-bit time stamps. This value defines the number of bits used to store data per time stamp.</p>
<p>To reduce the cost of formatting the data, the driver can include junk values in the 64-bit time stamps. For example, the driver could write 64-bit time stamps with 55 valid bits of precision. In this case the upper 9 bits are considered junk values and are stripped off by ETW.</p>
</td>
</tr>
</table>
<p> </p>
<p>Values between 0 and 32 are unsupported and invalid.</p>
<p>If the hardware supports 64-bit time stamps but only 32 bits are usable, the driver must ensure that the data is presented correctly to the DirectX graphics kernel subsystem. If the driver has no other alternatives to present the data, it should provide the precision value when the <a href="display.dxgkddiformathistorybuffer">DxgkDdiFormatHistoryBuffer</a> function is next called.</p>
</dd>
</dl>

## -remarks
<p>In a call to the <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function, the output data size,  <a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>.<b>OutputDataSize</b>, is:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="display.dxgkddiformathistorybuffer">DxgkDdiFormatHistoryBuffer</a>
</dt>
<dt>
<a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_HISTORYBUFFERPRECISION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
