---
UID: NS:d3dhal._D3DHAL_CONTEXTCREATEDATA
title: "_D3DHAL_CONTEXTCREATEDATA"
author: windows-driver-content
description: The D3DHAL_CONTEXTCREATEDATA structure contains all of the information that the D3dContextCreate function requires to create a new context.
old-location: display\d3dhal_contextcreatedata.htm
old-project: display
ms.assetid: 9ad169a8-81a7-497c-849a-c36be66caa8e
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*LPD3DHAL_CONTEXTCREATEDATA, D3DHAL_CONTEXTCREATEDATA, D3DHAL_CONTEXTCREATEDATA structure [Display Devices], LPD3DHAL_CONTEXTCREATEDATA, LPD3DHAL_CONTEXTCREATEDATA structure pointer [Display Devices], _D3DHAL_CONTEXTCREATEDATA, d3dhal/D3DHAL_CONTEXTCREATEDATA, d3dhal/LPD3DHAL_CONTEXTCREATEDATA, d3dstrct_46c9dd06-302d-423b-8cd6-fc81a4227ab4.xml, display.d3dhal_contextcreatedata"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dhal.h
api_name:
-	D3DHAL_CONTEXTCREATEDATA
product: Windows
targetos: Windows
req.typenames: D3DHAL_CONTEXTCREATEDATA
---

# _D3DHAL_CONTEXTCREATEDATA structure
The D3DHAL_CONTEXTCREATEDATA structure contains all of the information that the <a href="..\d3dhal\nc-d3dhal-lpd3dhal_contextcreatecb.md">D3dContextCreate</a> function requires to create a new context.

## Syntax
````
typedef struct _D3DHAL_CONTEXTCREATEDATA {
  union {
    LPDDRAWI_DIRECTDRAW_GBL lpDDGbl;
    LPDDRAWI_DIRECTDRAW_LCL lpDDLcl;
  };
  union {
    LPDIRECTDRAWSURFACE       lpDDS;
    LPDDRAWI_DDRAWSURFACE_LCL lpDDSLcl;
  };
  union {
    LPDIRECTDRAWSURFACE       lpDDSZ;
    LPDDRAWI_DDRAWSURFACE_LCL lpDDSZLcl;
  };
  union {
    DWORD     dwPID;
    ULONG_PTR dwrstates;
  };
  ULONG_PTR dwhContext;
  HRESULT   ddrval;
} D3DHAL_CONTEXTCREATEDATA, *LPD3DHAL_CONTEXTCREATEDATA;
````

## Members


`ddrval`

Specifies the location where the driver writes the return code for <a href="..\d3dhal\nc-d3dhal-lpd3dhal_contextcreatecb.md">D3dContextCreate</a>. A return code of D3D_OK indicates success. A return code of D3DHAL_OUTOFCONTEXTS indicates that the driver cannot create the context. For more information, see <a href="https://msdn.microsoft.com/033beb6e-5872-4cb3-8f39-459e2fff82cd">Return Codes for Direct3D Driver Callbacks</a>.

`dwhContext`

Specifies a location that indicates, on input, the version of the Direct3D user-mode runtime and, on output, where the driver returns the context handle upon successfully creating the context. See Remarks for more information.

## Remarks
When the Direct3D runtime calls the driver's <a href="..\d3dhal\nc-d3dhal-lpd3dhal_contextcreatecb.md">D3dContextCreate</a> function, the runtime specifies a number that indicates the runtime's user-mode version in the <b>dwhContext</b> member. The following table shows a mapping of numbers and user-mode versions.

<table>
<tr>
<th>Number</th>
<th>DirectX user-mode version</th>
</tr>
<tr>
<td>
5

</td>
<td>
9.0

</td>
</tr>
<tr>
<td>
4

</td>
<td>
8.0

</td>
</tr>
<tr>
<td>
3

</td>
<td>
7.0

</td>
</tr>
<tr>
<td>
2

</td>
<td>
6.0

</td>
</tr>
<tr>
<td>
1

</td>
<td>
5.0

</td>
</tr>
<tr>
<td>
0

</td>
<td>
3.0

</td>
</tr>
</table>
 

If the driver successfully creates a context, the driver returns the context ID in <b>dwhContext</b> for the Direct3D runtime to use when communicating with the driver.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dhal.h (include D3dhal.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550595">DD_DIRECTDRAW_LOCAL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551733">DD_SURFACE_LOCAL</a>



<a href="..\d3dhal\nc-d3dhal-lpd3dhal_contextcreatecb.md">D3dContextCreate</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_CONTEXTCREATEDATA structure%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>