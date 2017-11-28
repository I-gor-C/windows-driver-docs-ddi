---
UID: NS.d3dhal._D3DHAL_DRAWPRIMITIVES2DATA
title: D3DHAL_DRAWPRIMITIVES2DATA
author: windows-driver-content
description: The D3DHAL_DRAWPRIMITIVES2DATA structure contains the information required by the D3dDrawPrimitives2 function to render primitives.
old-location: display\d3dhal_drawprimitives2data.htm
old-project: display
ms.assetid: d971e866-3049-4722-bfec-ca3364f291fd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DRAWPRIMITIVES2DATA, D3DHAL_DRAWPRIMITIVES2DATA
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
req.alt-api: D3DHAL_DRAWPRIMITIVES2DATA
req.alt-loc: d3dhal.h
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

# D3DHAL_DRAWPRIMITIVES2DATA structure



## -description
<p>The D3DHAL_DRAWPRIMITIVES2DATA structure contains the information required by the <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a> function to render primitives.</p>


## -syntax

````
typedef struct _D3DHAL_DRAWPRIMITIVES2DATA {
  ULONG_PTR                 dwhContext;
  DWORD                     dwFlags;
  DWORD                     dwVertexType;
  LPDDRAWI_DDRAWSURFACE_LCL lpDDCommands;
  DWORD                     dwCommandOffset;
  DWORD                     dwCommandLength;
  union {
    LPDDRAWI_DDRAWSURFACE_LCL lpDDVertex;
    LPVOID                    lpVertices;
  };
  DWORD                     dwVertexOffset;
  DWORD                     dwVertexLength;
  DWORD                     dwReqVertexBufSize;
  DWORD                     dwReqCommandBufSize;
  LPDWORD                   lpdwRStates;
  union {
    DWORD   dwVertexSize;
    HRESULT ddrval;
  };
  DWORD                     dwErrorOffset;
} D3DHAL_DRAWPRIMITIVES2DATA, *LPD3DHAL_DRAWPRIMITIVES2DATA;
````


## -struct-fields
<dl>

### -field <b>dwhContext</b>

<dd>
<p>Specifies the context handle of the Direct3D device.</p>
</dd>

### -field <b>dwFlags</b>

<dd>
<p>Specifies flags that provide additional instructions to the driver or provide information from the driver. This member can be a bitwise OR of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DHALDP2_EXECUTEBUFFER</p>
</td>
<td>
<p>The command and vertex buffers were created in system memory. The driver should update the state array that <b>lpdwRStates</b> points to. This flag is set by Direct3D only.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_REQCOMMANDBUFSIZE</p>
</td>
<td>
<p>The driver must be able to increase the current command buffer by at least the size specified in <b>dwReqCommandBufSize</b>. Drivers that do not support multibuffering of command buffers can ignore this flag. This flag is set by Direct3D only.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_REQVERTEXBUFSIZE</p>
</td>
<td>
<p>The driver must be able to allocate a vertex buffer of at least the size specified in <b>dwReqCommandBufSize</b>. Drivers that do not support multibuffering of vertex buffers can ignore this flag. This flag is set by Direct3D only.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_SWAPCOMMANDBUFFER</p>
</td>
<td>
<p>The driver can swap the buffer that <b>lpDDCommands</b> points to with a new command buffer and return immediately, asynchronously processing the original buffer while Direct3D fills the new command buffer. Drivers that do not support multibuffering of command buffers can ignore this flag. This flag is set by Direct3D only.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_SWAPVERTEXBUFFER</p>
</td>
<td>
<p>The driver can swap the buffer that <b>lpDDVertex</b> or <b>lpVertices</b> points to with a new vertex buffer and return immediately, asynchronously processing the original buffer while Direct3D fills the new vertex buffer. Drivers that do not support multibuffering of vertex buffers can ignore this flag. This flag is set by Direct3D only.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_USERMEMVERTICES</p>
</td>
<td>
<p>The <b>lpVertices</b> member is valid so the driver should obtain the vertex data from the user-allocated memory that <b>lpVertices</b> points to. This flag is set by Direct3D only.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_VIDMEMCOMMANDBUF</p>
</td>
<td>
<p>The command buffer allocated by the driver as a swap buffer is not in system memory. This flag can be set by drivers that support multibuffering of command buffers.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHALDP2_VIDMEMVERTEXBUF</p>
</td>
<td>
<p>The vertex buffer allocated by the driver as a swap buffer is not in system memory. This flag can be set by drivers that support multibuffering of vertex buffers.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwVertexType</b>

<dd>
<p>Identifies the <a href="https://msdn.microsoft.com/206f4275-bcb8-4e8e-9c11-c6fb5d9c561d">FVF</a> of the data in the vertex buffer; that is, <b>dwVertexType</b> specifies which per-vertex data fields are present in the vertex buffer that <b>lpDDVertex</b> or <b>lpVertices</b> points to. This member can be a bitwise OR of the values in the following table. Only one of the <i>D3DFVF_TEXx</i> flags is set.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DFVF_DIFFUSE</p>
</td>
<td>
<p>Each vertex has a diffuse color.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_SPECULAR</p>
</td>
<td>
<p>Each vertex has a specular color.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX0</p>
</td>
<td>
<p>No texture coordinates are provided with the vertex data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX1</p>
</td>
<td>
<p>Each vertex has one set of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX2</p>
</td>
<td>
<p>Each vertex has two sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX3</p>
</td>
<td>
<p>Each vertex has three sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX4</p>
</td>
<td>
<p>Each vertex has four sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX5</p>
</td>
<td>
<p>Each vertex has five sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX6</p>
</td>
<td>
<p>Each vertex has six sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX7</p>
</td>
<td>
<p>Each vertex has seven sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_TEX8</p>
</td>
<td>
<p>Each vertex has eight sets of texture coordinates.</p>
</td>
</tr>
<tr>
<td>
<p>D3DFVF_XYZRHW</p>
</td>
<td>
<p>Each vertex has <i>x, y, z,</i> and <i>w</i> coordinates. This flag is always set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>lpDDCommands</b>

<dd>
<dl>

### -field <b>DirectX 8.1 and earlier versions only.
      </b>


### -field Points to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551733">DD_SURFACE_LOCAL</a> structure that identifies the DirectDraw surface containing the command data. The <b>fpVidMem</b> member of the embedded <a href="https://msdn.microsoft.com/library/windows/hardware/ff551726">DD_SURFACE_GLOBAL</a> structure points to the buffer that contains state change and primitive drawing commands for the driver to process. Specifically, this buffer contains one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a> structures, each followed by a <i>D3DHAL_DP2Xxx</i> structure whose exact type is identified by D3DHAL_DP2COMMAND's <b>bCommand</b> member.


### -field <b>DirectX 9.0 and later versions only.</b>


### -field In addition to the command-buffer functionality of DirectX 8.1 and earlier, this member can point to a response buffer that the driver returns. Specifically, this response buffer contains one or more <a href="https://msdn.microsoft.com/library/windows/hardware/ff545710">D3DHAL_DP2RESPONSE</a> structures, each followed by either <a href="https://msdn.microsoft.com/library/windows/hardware/ff545714">D3DHAL_DP2RESPONSEQUERY</a> structures or zero if the response token in the <b>bCommand</b> of D3DHAL_DP2RESPONSE is D3DDP2OP_RESPONSECONTINUE.

</dl>
</dd>

### -field <b>dwCommandOffset</b>

<dd>
<dl>

### -field <b>DirectX 8.1 and earlier versions only.</b>


### -field Specifies the number of bytes into the surface that <b>lpDDCommands</b> points to and where the command data starts.


### -field <b>DirectX 9.0 and later versions only.</b>


### -field In addition to the command-offset functionality of DirectX 8.1 and earlier, can specify where the response data starts.

</dl>
</dd>

### -field <b>dwCommandLength</b>

<dd>
<p>Specifies the number of bytes of valid command data in the surface that <b>lpDDCommands</b> points to starting at <b>dwCommandOffset</b>.</p>
</dd>

### -field <b>lpDDVertex</b>

<dd>
<p>Points to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551733">DD_SURFACE_LOCAL</a> structure that identifies the DirectDraw surface containing the vertex data when the D3DHALDP2_USERMEMVERTICES flag is not set in <b>dwFlags</b>. Forms a union with <b>lpVertices</b>. </p>
</dd>

### -field <b>lpVertices</b>

<dd>
<p>Points to a user-mode memory block containing vertex data when the D3DHALDP2_USERMEMVERTICES flag is set in <b>dwFlags</b>.</p>
</dd>

### -field <b>dwVertexOffset</b>

<dd>
<p>Specifies the number of bytes into the surface pointed to by <b>lpDDVertex</b> or <b>lpVertices</b> where the vertex data starts.</p>
</dd>

### -field <b>dwVertexLength</b>

<dd>
<p>Specifies the number of vertices for which valid data exists in the surface pointed to by <b>lpDDVertex</b> or <b>lpVertices</b>. This valid data starts at <b>dwVertexOffset</b>.</p>
</dd>

### -field <b>dwReqVertexBufSize</b>

<dd>
<p>Specifies the minimum number of bytes that the driver must allocate for the swap vertex buffer. This member is valid only when the D3DHALDP2_REQVERTEXBUFSIZE flag is set. Drivers that do not support multibuffering of vertex buffers should ignore this member.</p>
</dd>

### -field <b>dwReqCommandBufSize</b>

<dd>
<p>Specifies the minimum number of bytes that the driver must increase the swap command buffer by. This member is valid only when the D3DHALDP2_REQCOMMANDBUFSIZE flag is set. Drivers that do not support multibuffering of command buffers should ignore this member.</p>
</dd>

### -field <b>lpdwRStates</b>

<dd>
<p>Points to a render state array that the driver should update when it parses render state commands from the command buffer. The driver should update this array only when the D3DHALDP2_EXECUTEBUFFER flag is set in <b>dwFlags</b>. The driver should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549036">D3DRENDERSTATETYPE</a> enumerated types to update the appropriate element of the render state array. </p>
</dd>

### -field <b>dwVertexSize</b>

<dd>
<p>Specifies the size of each vertex, in bytes. This member forms a union with <b>ddrval</b>.</p>
</dd>

### -field <b>ddrval</b>

<dd>
<p>Specifies the location where the driver writes the return value of <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>. D3D_OK indicates success. Otherwise, the driver should return the appropriate D3DERR_<i>Xxx</i> error code. For more information, see <a href="https://msdn.microsoft.com/033beb6e-5872-4cb3-8f39-459e2fff82cd">Return Codes for Direct3D Driver Callbacks</a>.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3D_OK</p>
</td>
<td>
<p>The operation completed successfully.</p>
</td>
</tr>
<tr>
<td>
<p>D3DERR_COMMAND_UNPARSED</p>
</td>
<td>
<p>The driver requires the Direct3D runtime to parse the execute buffer.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwErrorOffset</b>

<dd>
<dl>

### -field <b>DirectX 8.1 and earlier versions only.</b>


### -field Specifies the location where the driver writes the offset into the surface that <b>lpDDCommands</b> points to where the first unhandled D3DHAL_DP2COMMAND can be found. The driver must set this value when it returns an error condition in <b>ddrval</b>.


### -field <b>DirectX 9.0 and later versions only.</b>


### -field In addition to the error-offset functionality of DirectX 8.1 and earlier, the driver can specify the total size, in bytes, of the outgoing response buffer or zero if the response buffer is empty of responses. This member specifies response-buffer information only when the <b>ddrval</b> member is set to D3D_OK for successful completion. If this member is nonzero, it indicates that previously submitted queries using the D3DDP2OP_ISSUEQUERY operation completed and that responses to those queries are specified in <a href="https://msdn.microsoft.com/library/windows/hardware/ff545710">D3DHAL_DP2RESPONSE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545714">D3DHAL_DP2RESPONSEQUERY</a> structures and available in the outgoing response buffer. Each D3DHAL_DP2RESPONSEQUERY is followed by the following data related to the query: 


### -field BOOL for D3DQUERYTYPE_EVENT 


### -field DWORD for D3DQUERYTYPE_OCCLUSION


### -field 
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544702">D3DDEVINFO_VCACHE</a> structure for D3DQUERYTYPE_VCACHE


### -field The runtime parses the response buffer and updates its internal data structures.


### -field If this member is zero and the <b>ddrval</b> member is set to D3D_OK, the runtime does not bother to check for responses to queries. 

</dl>
</dd>
</dl>

## -remarks
<p>Note that the <b>dwVertexOffset</b> member specifies values in bytes; the <b>dwVertexLength</b> member specifies values in vertices. </p>

<p>To calculate the valid data, in bytes, that exists in the surface at <b>lpDDVertex</b> or <b>lpVertices</b>, multiply the value in <b>dwVertexLength</b> by the value in <b>dwVertexSize</b>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545454">D3DHAL_DP2COMMAND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549036">D3DRENDERSTATETYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551726">DD_SURFACE_GLOBAL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551733">DD_SURFACE_LOCAL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DRAWPRIMITIVES2DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
