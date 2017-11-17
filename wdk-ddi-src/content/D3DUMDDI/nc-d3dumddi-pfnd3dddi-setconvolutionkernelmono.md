---
UID: NC.d3dumddi.PFND3DDDI_SETCONVOLUTIONKERNELMONO
title: PFND3DDDI_SETCONVOLUTIONKERNELMONO
author: windows-driver-content
description: The SetConvolutionKernelMono function defines the resolution and weights of the kernel filter, which is used when the D3DTEXF_CONVOLUTIONMONO texture filtering mode is set.
old-location: display\setconvolutionkernelmono.htm
ms.assetid: b560352f-ca4e-4f03-88ac-13ec080834aa
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetConvolutionKernelMono
req.alt-loc: d3dumddi.h
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_SETCONVOLUTIONKERNELMONO callback



## -description
<p>The <i>SetConvolutionKernelMono</i> function defines the resolution and weights of the kernel filter, which is used when the D3DTEXF_CONVOLUTIONMONO texture filtering mode is set.</p>


## -prototype

````
PFND3DDDI_SETCONVOLUTIONKERNELMONO SetConvolutionKernelMono;

__checkReturn HRESULT APIENTRY SetConvolutionKernelMono(
  _In_       HANDLE                             hDevice,
  _In_ const D3DDDIARG_SETCONVOLUTIONKERNELMONO *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543285">D3DDDIARG_SETCONVOLUTIONKERNELMONO</a> structure that describes parameters for setting the monochrome convolution kernel.</p>
</dd>
</dl>

## -returns
<p><i>SetConvolutionKernelMono</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The monochrome convolution kernel is successfully set.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>SetConvolutionKernelMono</i> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks
<p>D3DTEXF_CONVOLUTIONMONO is a texture filter mode that is used for sampling monochrome textures (that is, textures that are formatted as one bit per pixel (D3DDDIFMT_A1)). In the Direct3D 9.L runtime, the convolution filter is a two-dimensional box filter (that is, all weights = 1.0). However, the <i>SetConvolutionKernelMono</i> function is defined to support a more general filter. When D3DTEXF_CONVOLUTIONMONO is set to a texture sampler, the texture sampler states D3DTSS_MIPFILTER, D3DTSS_MINFILTER and D3DTSS_MAGFILTER are ignored. The texture address D3DTADDRESS_BORDER with border color 0 should be applied in this filtering mode. The user-mode display driver should return an error or ignore the rendered primitive if this filtering mode is used with a non-monochrome texture.</p>

<p>The following formula is used to perform the convolution:</p>

<p>Result = Sum(i=0, i &lt;N<sub>v</sub>)[ (R<sub>i</sub>*(1 - alpha) + R<sub>i+1</sub>*alpha) * S)]</p>

<p>Rₖ = Sum(j=0, j &lt;N<sub>u</sub>)[T<sub>k,j</sub>*(1 - beta) + T<sub>k,j+1</sub>*beta],  where 0 &lt; k &lt; N<sub>v</sub></p>

<p>S = 1 / (N<sub>u</sub> * N<sub>v</sub>)</p>

<p>N<sub>u</sub> and N<sub>v</sub> are the width and height of the filter kernel.</p>

<p>T<sub>i,j</sub> are texture samples from a monochrome texture at location (i, j).</p>

<p>The precision of the filter operations must be at least 6 bits.</p>

<p>The interpolated texture coordinate values (U, V) at a pixel center are the coordinates of the center of the filter kernel.</p>

<p>The coordinates of the upper left filter kernel sample (U<sub>f</sub>,V<sub>f</sub>) are computed as:</p>

<p>U<sub>f</sub> = U * TextureWidth - N<sub>u</sub> * 0.5</p>

<p>V<sub>f </sub>= V * TextureHeight - N<sub>v</sub> * 0.5</p>

<p>Then</p>

<p>beta = U<sub>f</sub> - truncate(U<sub>f</sub>)</p>

<p>alpha = V<sub>f</sub> - truncate(V<sub>f</sub>)</p>

<p>D3DTEXF_CONVOLUTIONMONO is a texture filter mode that is used for sampling monochrome textures (that is, textures that are formatted as one bit per pixel (D3DDDIFMT_A1)). In the Direct3D 9.L runtime, the convolution filter is a two-dimensional box filter (that is, all weights = 1.0). However, the <i>SetConvolutionKernelMono</i> function is defined to support a more general filter. When D3DTEXF_CONVOLUTIONMONO is set to a texture sampler, the texture sampler states D3DTSS_MIPFILTER, D3DTSS_MINFILTER and D3DTSS_MAGFILTER are ignored. The texture address D3DTADDRESS_BORDER with border color 0 should be applied in this filtering mode. The user-mode display driver should return an error or ignore the rendered primitive if this filtering mode is used with a non-monochrome texture.</p>

<p>The following formula is used to perform the convolution:</p>

<p>Result = Sum(i=0, i &lt;N<sub>v</sub>)[ (R<sub>i</sub>*(1 - alpha) + R<sub>i+1</sub>*alpha) * S)]</p>

<p>Rₖ = Sum(j=0, j &lt;N<sub>u</sub>)[T<sub>k,j</sub>*(1 - beta) + T<sub>k,j+1</sub>*beta],  where 0 &lt; k &lt; N<sub>v</sub></p>

<p>S = 1 / (N<sub>u</sub> * N<sub>v</sub>)</p>

<p>N<sub>u</sub> and N<sub>v</sub> are the width and height of the filter kernel.</p>

<p>T<sub>i,j</sub> are texture samples from a monochrome texture at location (i, j).</p>

<p>The precision of the filter operations must be at least 6 bits.</p>

<p>The interpolated texture coordinate values (U, V) at a pixel center are the coordinates of the center of the filter kernel.</p>

<p>The coordinates of the upper left filter kernel sample (U<sub>f</sub>,V<sub>f</sub>) are computed as:</p>

<p>U<sub>f</sub> = U * TextureWidth - N<sub>u</sub> * 0.5</p>

<p>V<sub>f </sub>= V * TextureHeight - N<sub>v</sub> * 0.5</p>

<p>Then</p>

<p>beta = U<sub>f</sub> - truncate(U<sub>f</sub>)</p>

<p>alpha = V<sub>f</sub> - truncate(V<sub>f</sub>)</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543285">D3DDDIARG_SETCONVOLUTIONKERNELMONO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETCONVOLUTIONKERNELMONO callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
