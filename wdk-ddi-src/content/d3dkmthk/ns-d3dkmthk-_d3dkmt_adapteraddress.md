---
UID: NS.D3DKMTHK._D3DKMT_ADAPTERADDRESS
title: _D3DKMT_ADAPTERADDRESS
author: windows-driver-content
description: The D3DKMT_ADAPTERADDRESS structure describes the physical location of the graphics adapter.
old-location: display\d3dkmt_adapteraddress.htm
old-project: display
ms.assetid: 70f45ca2-4be6-4e74-b2e8-55ef7a43192f
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _D3DKMT_ADAPTERADDRESS, D3DKMT_ADAPTERADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_ADAPTERADDRESS
req.alt-loc: d3dkmthk.h
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
---

# _D3DKMT_ADAPTERADDRESS structure



## -description
The D3DKMT_ADAPTERADDRESS structure describes the physical location of the graphics adapter. 



## -syntax

````
typedef struct _D3DKMT_ADAPTERADDRESS {
  UINT BusNumber;
  UINT DeviceNumber;
  UINT FunctionNumber;
} D3DKMT_ADAPTERADDRESS;
````


## -struct-fields

### -field BusNumber

[out] The number of the bus that the graphics adapter's physical device is located on.


### -field DeviceNumber

[out] The index of the graphics adapter's physical device on the bus.


### -field FunctionNumber

[out] The function number of the graphics adapter on the physical device.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_queryadapterinfo">D3DKMT_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="display.d3dkmtqueryadapterinfo">D3DKMTQueryAdapterInfo</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_ADAPTERADDRESS structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

