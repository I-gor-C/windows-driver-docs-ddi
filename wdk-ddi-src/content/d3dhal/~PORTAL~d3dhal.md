# Declarations in the d3dhal header
This header D3Dhal contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [D3DHAL_DP2UPDATEPALETTE structure](ns-d3dhal--d3dhal-dp2updatepalette.md) | The D3DHAL_DP2UPDATEPALETTE structure alters the palette that is used for palletized textures. |
| [D3DHAL_TEXTURESWAPDATA structure](ns-d3dhal--d3dhal-textureswapdata.md) | TBD |
| [D3DHAL_DP2ZRANGE structure](ns-d3dhal--d3dhal-dp2zrange.md) | The D3DHAL_DP2ZRANGE structure specifies z-range minimum and maximum in D3dDrawPrimitives2. |
| [DD_GETEXTENDEDMODEDATA structure](ns-d3dhal--dd-getextendedmodedata.md) | DirectX 9.0 and later versions only. DD_GETEXTENDEDMODEDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETEXTENDEDMODE. |
| [D3DHAL_DP2SETCONVOLUTIONKERNELMONO structure](ns-d3dhal--d3dhal-dp2setconvolutionkernelmono.md) | TBD |
| [DD_GETFORMATDATA structure](ns-d3dhal--dd-getformatdata.md) | DD_GETFORMATDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETFORMAT. |
| [D3DHAL_DP2WINFO structure](ns-d3dhal--d3dhal-dp2winfo.md) | The D3DHAL_DP2WINFO structure is used to inform the driver of the w-range to be used for w-buffering. |
| [D3DHAL_CALLBACKS2 structure](ns-d3dhal--d3dhal-callbacks2~r1.md) | TBD |
| [D3DHAL_CALLBACKS structure](ns-d3dhal--d3dhal-callbacks.md) | TBD |
| [D3DHAL_VALIDATETEXTURESTAGESTATEDATA structure](ns-d3dhal--d3dhal-validatetexturestagestatedata.md) | The D3DHAL_VALIDATETEXTURESTAGESTATEDATA structure contains the information required for the driver to determine and return its ability to support multitexturing using the current state. |
| [D3DHAL_TEXTUREGETSURFDATA structure](ns-d3dhal--d3dhal-texturegetsurfdata.md) | TBD |
| [DD_GETD3DQUERYCOUNTDATA structure](ns-d3dhal--dd-getd3dquerycountdata.md) | DirectX 9.0 and later versions only. DD_GETD3DQUERYCOUNTDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETD3DQUERYCOUNT. |
| [D3DHAL_DRAWONEINDEXEDPRIMITIVEDATA structure](ns-d3dhal--d3dhal-drawoneindexedprimitivedata.md) | TBD |
| [D3DHAL_DP2INDEXEDTRIANGLELIST2 structure](ns-d3dhal--d3dhal-dp2indexedtrianglelist2.md) | One or more D3DHAL_DP2INDEXEDTRIANGLELIST2 structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDTRIANGLELIST2, and are used to render a sequence of unconnected triangles using vertex indices. |
| [D3DHAL_CONTEXTCREATEDATA structure](ns-d3dhal--d3dhal-contextcreatedata.md) | The D3DHAL_CONTEXTCREATEDATA structure contains all of the information that the D3dContextCreate function requires to create a new context. |
| [D3DHAL_D3DDX6EXTENDEDCAPS structure](ns-d3dhal--d3dhal-d3ddx6extendedcaps.md) | TBD |
| [D3DDeviceDesc_V2 structure](ns-d3dhal--d3ddevicedesc-v2.md) | TBD |
| [D3DHAL_CALLBACKS3 structure](ns-d3dhal--d3dhal-callbacks3.md) | TBD |
| [D3DHAL_CALLBACKS2 structure](ns-d3dhal--d3dhal-callbacks2~r2.md) | TBD |
| [D3DDeviceDesc_V1 structure](ns-d3dhal--d3ddevicedesc-v1.md) | Obsolete in DirectX 8.0 and later versions; see Remarks. The D3DDEVICEDESC_V1 structure describes the 3D capabilities of a device. |
| [D3DHAL_DP2SETVERTEXSHADERCONST structure](ns-d3dhal--d3dhal-dp2setvertexshaderconst.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2SETVERTEXSHADERCONST structure is used to set one or more of the vertex shader constant registers when the D3DDP2OP_SETVERTEXSHADERCONST opcode is received by D3dDrawPrimitives2. |
| [D3DHAL_DP2SETTRANSFORM structure](ns-d3dhal--d3dhal-dp2settransform.md) | D3DHAL_DP2SETTRANSFORM structure is used to specify the transform state and matrix for D3dDrawPrimitives2. |
| [DD_MULTISAMPLEQUALITYLEVELSDATA structure](ns-d3dhal--dd-multisamplequalitylevelsdata.md) | DirectX 9.0 and later versions only. DD_MULTISAMPLEQUALITYLEVELSDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETMULTISAMPLEQUALITYLEVELS. |
| [D3DHAL_SETRENDERTARGETDATA structure](ns-d3dhal--d3dhal-setrendertargetdata.md) | TBD |
| [D3DHAL_GETSTATEDATA structure](ns-d3dhal--d3dhal-getstatedata.md) | TBD |
| [D3DHAL_DP2VIEWPORTINFO structure](ns-d3dhal--d3dhal-dp2viewportinfo.md) | The D3DHAL_DP2VIEWPORTINFO structure is used to inform guard-band aware drivers of the view clipping rectangle. The clipping rectangle is specified by the members dwX, dwY, dwWidth and dwHeight. |
| [D3DHAL_DP2DRAWPRIMITIVE2 structure](ns-d3dhal--d3dhal-dp2drawprimitive2.md) | DirectX 8.0 and later versions only. D3DHAL_DRAWPRIMITIVE2 is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_DRAWPRIMITIVE2, and is used to render a primitive. |
| [D3DHAL_CONTEXTDESTROYALLDATA structure](ns-d3dhal--d3dhal-contextdestroyalldata.md) | TBD |
| [D3DCAPS8 structure](ns-d3dhal--d3dcaps8.md) | TBD |
| [D3DHAL_DP2SETPRIORITY structure](ns-d3dhal--d3dhal-dp2setpriority.md) | The D3DHAL_DP2SETPRIORITY structure is used to inform the driver of the priority of the texture specified by the handle dwDDDestSurface. |
| [D3DDeviceDesc_V3 structure](ns-d3dhal--d3ddevicedesc-v3.md) | TBD |
| [D3DHAL_DP2SETLIGHT structure](ns-d3dhal--d3dhal-dp2setlight.md) | The D3DHAL_DP2SETLIGHT structure allows lights to be set for D3dDrawPrimitives2. |
| [D3DHAL_DP2BUFFERBLT structure](ns-d3dhal--d3dhal-dp2bufferblt.md) | DirectX 8.0 and later versions only. D3DHAL_DP2BUFFERBLT is used for vertex or index buffer blts when D3dDrawPrimitives2 responds to the D3DDP2OP_BUFFERBLT command token. |
| [D3DHAL_DP2SETDEPTHSTENCIL structure](ns-d3dhal--d3dhal-dp2setdepthstencil.md) | DirectX 9.0 and later versions only. The D3DHAL_DP2SETDEPTHSTENCIL structure is used to map a new depth buffer in the driver's current context when the D3DDP2OP_SETDEPTHSTENCIL operation code is received by D3dDrawPrimitives2. |
| [D3DHAL_DP2TRIANGLESTRIP structure](ns-d3dhal--d3dhal-dp2trianglestrip.md) | One D3DHAL_DP2TRIANGLESTRIP structure is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_TRIANGLESTRIP, and is used to render the specified connected triangle strip. |
| [D3DHAL_DP2LINESTRIP structure](ns-d3dhal--d3dhal-dp2linestrip.md) | One D3DHAL_DP2LINESTRIP structure is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_LINESTRIP, and is used to render the specified connected line segments. |
| [D3DHAL_DRAWONEPRIMITIVEDATA structure](ns-d3dhal--d3dhal-drawoneprimitivedata.md) | TBD |
| [D3DHAL_DP2TRIANGLELIST structure](ns-d3dhal--d3dhal-dp2trianglelist.md) | One D3DHAL_DP2TRIANGLELIST structure is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_TRIANGLELIST, and is used to render the specified unconnected triangles. |
| [D3DHAL_DP2SETSTREAMSOURCEFREQ structure](ns-d3dhal--d3dhal-dp2setstreamsourcefreq.md) | DirectX 9.0 and later versions only. The D3DHAL_DP2SETSTREAMSOURCEFREQ structure is used to set the frequency divisor of a stream source that is bound to a vertex buffer for D3dDrawPrimitives2. |
| [D3DHAL_DP2COMMAND structure](ns-d3dhal--d3dhal-dp2command.md) | One or more D3DHAL_DP2COMMAND structures are parsed from the command buffer by the D3dDrawPrimitives2 callback, which uses the information it receives to draw one or more primitives. |
| [D3DHAL_DP2CREATEVERTEXSHADERDECL structure](ns-d3dhal--d3dhal-dp2createvertexshaderdecl.md) | DirectX 9.0 and later versions only. The D3DHAL_DP2CREATEVERTEXSHADERDECL structure is used to create a vertex shader declaration when a D3DDP2OP_CREATEVERTEXSHADERDECL opcode is received by D3dDrawPrimitives2. |
| [D3DHAL_DP2SETRENDERTARGET2 structure](ns-d3dhal--d3dhal-dp2setrendertarget2.md) | The D3DHAL_DP2SETRENDERTARGET2 structure is used with the D3DDP2OP_SETRENDERTARGET2 opcode to map a portion of a rendering target surface and depth buffer in the current context. |
| [D3DHAL_DP2INDEXEDTRIANGLESTRIP structure](ns-d3dhal--d3dhal-dp2indexedtrianglestrip.md) | One or more D3DHAL_DP2INDEXEDTRIANGLESTRIP structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDTRIANGLESTRIP, and are used to render strips of connected triangles using vertex indices. |
| [D3DHAL_CALLBACKS2 structure](ns-d3dhal--d3dhal-callbacks2.md) | TBD |
| [D3DHAL_SCENECAPTUREDATA structure](ns-d3dhal--d3dhal-scenecapturedata.md) | TBD |
| [DD_GETD3DQUERYDATA structure](ns-d3dhal--dd-getd3dquerydata.md) | DirectX 9.0 and later versions only. DD_GETD3DQUERYDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETD3DQUERY. |
| [D3DHAL_DP2SETINDICES structure](ns-d3dhal--d3dhal-dp2setindices.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2SETINDICES structure is used to set the current index buffer for D3dDrawPrimitives2. |
| [D3DHAL_DP2DRAWPRIMITIVE structure](ns-d3dhal--d3dhal-dp2drawprimitive.md) | DirectX 8.0 and later versions only. D3DHAL_DRAWPRIMITIVE is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_DRAWPRIMITIVE, and is used to render a primitive. |
| [D3DHAL_CALLBACKS structure](ns-d3dhal--d3dhal-callbacks~r2.md) | D3DHAL_CALLBACKS is one of several callback structures that describe the Direct3D support provided by the driver. |
| [D3DHAL_DP2DELETEQUERY structure](ns-d3dhal--d3dhal-dp2deletequery.md) | DirectX 9.0 and later versions only. |
| [D3DHAL_DP2PIXELSHADER structure](ns-d3dhal--d3dhal-dp2pixelshader.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2PIXELSHADER structure is used to set the current pixel shader, or delete a pixel shader, depending on the opcode received (D3DDP2OP_SETPIXELSHADER or D3DDP2OP_DELETEPIXELSHADER) by D3dDrawPrimitives2. |
| [DD_FREE_DEFERRED_AGP_DATA structure](ns-d3dhal--dd-free-deferred-agp-data.md) | DirectX 8.0 and later versions and NT-based operating systems only. DD_FREE_DEFERRED_AGP_DATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for D3DGDI2_TYPE_DEFER_AGP_FREES and D3DGDI2_TYPE_FREE_DEFERRED_AGP notifications. |
| [D3DHAL_DP2VOLUMEBLT structure](ns-d3dhal--d3dhal-dp2volumeblt.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2VOLUMEBLT structure is used for volume texture blts when D3dDrawPrimitives2 responds to the D3DDP2OP_VOLUMEBLT command token. |
| [D3DHAL_DP2EXT structure](ns-d3dhal--d3dhal-dp2ext.md) | The D3DHAL_DP2EXT structure's use has yet to be defined. |
| [D3DHAL_CALLBACKS structure](ns-d3dhal--d3dhal-callbacks~r1.md) | TBD |
| [D3DHAL_GLOBALDRIVERDATA structure](ns-d3dhal--d3dhal-globaldriverdata.md) | The D3DHAL_GLOBALDRIVERDATA structure specifies the 3D capabilities of the driver and its device. |
| [D3DHAL_DP2COMPOSERECTS structure](ns-d3dhal--d3dhal-dp2composerects.md) | TBD |
| [D3DHAL_DP2DRAWINDEXEDPRIMITIVE2 structure](ns-d3dhal--d3dhal-dp2drawindexedprimitive2.md) | DirectX 8.0 and later versions only. |
| [D3DHAL_DP2LINELIST structure](ns-d3dhal--d3dhal-dp2linelist.md) | One D3DHAL_DP2LINELIST structure is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_LINELIST, and is used to render unconnected line segments. |
| [D3DHAL_DP2COLORFILL structure](ns-d3dhal--d3dhal-dp2colorfill.md) | DirectX 9.0 and later versions only. D3DHAL_DP2COLORFILL is used for color-fill operations when D3dDrawPrimitives2 responds to the D3DDP2OP_COLORFILL command token. |
| [D3DHAL_RENDERPRIMITIVEDATA structure](ns-d3dhal--d3dhal-renderprimitivedata.md) | TBD |
| [DDRAWI_DDRAWSURFACE_LCL structure](ns-d3dhal--ddrawi-ddrawsurface-lcl.md) | TBD |
| [D3DHAL_DP2SURFACEBLT structure](ns-d3dhal--d3dhal-dp2surfaceblt.md) | DirectX 9.0 and later versions only. D3DHAL_DP2SURFACEBLT is used for two dimensional system memory to video memory surface blts when D3dDrawPrimitives2 responds to the D3DDP2OP_SURFACEBLT command token. |
| [DD_GETFORMATCOUNTDATA structure](ns-d3dhal--dd-getformatcountdata.md) | DirectX 8.0 and later versions only. DD_GETFORMATCOUNTDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETFORMATCOUNT. |
| [D3DHAL_DP2CREATEPIXELSHADER structure](ns-d3dhal--d3dhal-dp2createpixelshader.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2CREATEPIXELSHADER structure is used to create a pixel shader when a D3DDP2OP_CREATEPIXELSHADER opcode is received by D3dDrawPrimitives2. |
| [D3DHAL_DP2INDEXEDLINESTRIP structure](ns-d3dhal--d3dhal-dp2indexedlinestrip.md) | D3DHAL_DP2INDEXEDLINESTRIP is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDLINESTRIP, and is used to render a sequence of connected line segments using vertex indices. |
| [DD_GETDRIVERINFO2DATA structure](ns-d3dhal--dd-getdriverinfo2data.md) | DirectX 8.0 and later versions only. DD_GETDRIVERINFO2DATA is passed in the lpvData member of the DD_GETDRIVERINFODATA structure when GUID_GetDriverInfo2 is specified in the guidInfo member of DD_GETDRIVERINFODATA in a DdGetDriverInfo call. |
| [D3DHAL_DP2DRAWINDEXEDPRIMITIVE structure](ns-d3dhal--d3dhal-dp2drawindexedprimitive.md) | DirectX 8.0 and later versions only. |
| [DDRAWI_DDRAWSURFACE_LCL structure](ns-d3dhal--ddrawi-ddrawsurface-lcl~r1.md) | TBD |
| [D3DHAL_DP2ADDDIRTYBOX structure](ns-d3dhal--d3dhal-dp2adddirtybox.md) | DirectX 8.1 and later versions only. D3DHAL_DP2ADDDIRTYBOX is used to specify that a portion of a 3D resource--a volume texture--was dirtied in system memory. Therefore, this volume must be reloaded into video memory before being used. |
| [D3DHAL_RENDERSTATEDATA structure](ns-d3dhal--d3dhal-renderstatedata.md) | TBD |
| [DD_GETADAPTERGROUPDATA structure](ns-d3dhal--dd-getadaptergroupdata.md) | DirectX 9.0 and later versions only. DD_GETADAPTERGROUPDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETADAPTERGROUP. |
| [D3DHAL_DP2CREATEVERTEXSHADERFUNC structure](ns-d3dhal--d3dhal-dp2createvertexshaderfunc.md) | DirectX 9.0 and later versions only. The D3DHAL_DP2CREATEVERTEXSHADERFUNC structure is used to create a vertex shader code object when a D3DDP2OP_CREATEVERTEXSHADERFUNC opcode is received by D3dDrawPrimitives2. |
| [D3DHAL_DP2INDEXEDTRIANGLELIST structure](ns-d3dhal--d3dhal-dp2indexedtrianglelist.md) | One or more D3DHAL_DP2INDEXEDTRIANGLELIST structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDTRIANGLELIST, and are used to render a sequence of unconnected triangles using vertex indices. |
| [D3DHAL_DP2RENDERSTATE structure](ns-d3dhal--d3dhal-dp2renderstate.md) | One or more D3DHAL_DP2RENDERSTATE structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_RENDERSTATE, and are used to set the appropriate render state. |
| [D3DHAL_CLEAR2DATA structure](ns-d3dhal--d3dhal-clear2data.md) | TBD |
| [D3DHAL_CALLBACKS3 structure](ns-d3dhal--d3dhal-callbacks3~r2.md) | D3DHAL_CALLBACKS3 is one of several callback structures that describe the Direct3D support provided by the driver. |
| [DD_DXVERSION structure](ns-d3dhal--dd-dxversion.md) | DirectX 8.0 and later versions only. DD_DXVERSION describes the current DirectX runtime version. |
| [D3DHAL_DP2RESPONSE structure](ns-d3dhal--d3dhal-dp2response.md) | DirectX 9.0 and later versions only. |
| [D3DHAL_TEXTURECREATEDATA structure](ns-d3dhal--d3dhal-texturecreatedata.md) | TBD |
| [D3DHAL_DP2TRIANGLEFAN structure](ns-d3dhal--d3dhal-dp2trianglefan.md) | One D3DHAL_DP2TRIANGLEFAN structure is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_TRIANGLEFAN, and is used to render a triangle fan. |
| [D3DHAL_DP2BLT structure](ns-d3dhal--d3dhal-dp2blt.md) | DirectX 9.0 and later versions only. D3DHAL_DP2BLT is used for two dimensional surface blts when D3dDrawPrimitives2 responds to the D3DDP2OP_BLT command token. |
| [D3DHAL_DP2CLEAR structure](ns-d3dhal--d3dhal-dp2clear.md) | D3DHAL_DP2CLEAR contains all of the information that the driver needs to perform hardware-assisted clearing on the rendering target, depth buffer or stencil buffer. |
| [D3DHAL_DRAWPRIMITIVES2DATA structure](ns-d3dhal--d3dhal-drawprimitives2data.md) | The D3DHAL_DRAWPRIMITIVES2DATA structure contains the information required by the D3dDrawPrimitives2 function to render primitives. |
| [D3DHAL_DP2ADDDIRTYRECT structure](ns-d3dhal--d3dhal-dp2adddirtyrect.md) | DirectX 8.1 and later versions only. D3DHAL_DP2ADDDIRTYRECT is used to specify that a portion of a 2D resource--a 2D texture or cube texture--was dirtied in system memory. Therefore, this 2D texture must be reloaded into video memory before being used. |
| [D3DHAL_DP2SETPALETTE structure](ns-d3dhal--d3dhal-dp2setpalette.md) | The D3DHAL_DP2SETPALETTE structure is used to associate a palette with a texture when a driver responds to D3DDP2OP_SETPALETTE in D3dDrawPrimitives2. |
| [D3DHAL_DP2SETSTREAMSOURCE2 structure](ns-d3dhal--d3dhal-dp2setstreamsource2.md) | DirectX 9.0 and later versions only. The D3DHAL_DP2SETSTREAMSOURCE2 structure is used to bind a portion of a vertex stream source to a vertex buffer for D3dDrawPrimitives2. |
| [D3DHAL_DP2SETPIXELSHADERCONST structure](ns-d3dhal--d3dhal-dp2setpixelshaderconst.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2SETPIXELSHADERCONST structure is used to set one or more of the pixel shader constant registers when the D3DDP2OP_SETPIXELSHADERCONST opcode is received by D3dDrawPrimitives2. |
| [D3DHAL_DP2VERTEXSHADER structure](ns-d3dhal--d3dhal-dp2vertexshader.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2VERTEXSHADER structure sets the current vertex shader, or deletes a vertex shader, depending on the opcode received (D3DDP2OP_SETVERTEXSHADER or D3DDP2OP_DELETEVERTEXSHADER) by D3dDrawPrimitives2. |
| [D3DHAL_DP2CREATELIGHT structure](ns-d3dhal--d3dhal-dp2createlight.md) | The D3DHAL_DP2CREATELIGHT structure is used to create a light for D3dDrawPrimitives2. |
| [D3DHAL_DP2SETSTREAMSOURCEUM structure](ns-d3dhal--d3dhal-dp2setstreamsourceum.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2SETSTREAMSOURCEUM structure is used to bind a vertex stream source to a user memory buffer for D3dDrawPrimitives2. |
| [D3DHAL_DP2TEXBLT structure](ns-d3dhal--d3dhal-dp2texblt.md) | The D3DHAL_DP2TEXBLT structure is used for texture blts when D3dDrawPrimitives2 responds to the D3DDP2OP_TEXBLT command token. |
| [D3DHAL_D3DEXTENDEDCAPS structure](ns-d3dhal--d3dhal-d3dextendedcaps.md) | D3DHAL_D3DEXTENDEDCAPS describes additional 3D capabilities of the driver. |
| [D3DHAL_DP2DRAWRECTPATCH structure](ns-d3dhal--d3dhal-dp2drawrectpatch.md) | DirectX 8.0 and later versions only. |
| [DDRAWI_DIRECTDRAW_GBL structure](ns-d3dhal--ddrawi-directdraw-gbl.md) | TBD |
| [D3DHAL_DP2ISSUEQUERY structure](ns-d3dhal--d3dhal-dp2issuequery.md) | DirectX 9.0 and later versions only. |
| [DD_DEFERRED_AGP_AWARE_DATA structure](ns-d3dhal--dd-deferred-agp-aware-data.md) | DirectX 8.0 and later versions and NT-based operating systems only. DD_DEFERRED_AGP_AWARE_DATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for D3DGDI2_TYPE_DEFERRED_AGP_AWARE notifications. |
| [DD_GETEXTENDEDMODECOUNTDATA structure](ns-d3dhal--dd-getextendedmodecountdata.md) | DirectX 9.0 and later versions only. DD_GETEXTENDEDMODECOUNTDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETEXTENDEDMODECOUNT. |
| [D3DHAL_DP2STATESET structure](ns-d3dhal--d3dhal-dp2stateset.md) | The D3DHAL_DP2STATESET structure is used to inform the driver about stateset operations to perform. |
| [D3DHAL_DRAWPRIMITIVESDATA structure](ns-d3dhal--d3dhal-drawprimitivesdata.md) | TBD |
| [D3DHAL_CONTEXTDESTROYDATA structure](ns-d3dhal--d3dhal-contextdestroydata.md) | The D3DHAL_CONTEXTDESTROYDATA structure contains the information that the D3dContextDestroy function requires to delete a context. |
| [D3DHAL_DP2CREATEVERTEXSHADER structure](ns-d3dhal--d3dhal-dp2createvertexshader.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2CRED3dDrawPrimitives2ATEVERTEXSHADER structure is used to create a vertex shader when a D3DDP2OP_CREATEVERTEXSHADER opcode is received by . |
| [D3DHAL_DP2DRAWTRIPATCH structure](ns-d3dhal--d3dhal-dp2drawtripatch.md) | DirectX 8.0 and later versions only. |
| [D3DHAL_DP2SETSTREAMSOURCE structure](ns-d3dhal--d3dhal-dp2setstreamsource.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2SETSTREAMSOURCE structure is used to bind a vertex stream source to a vertex buffer for D3dDrawPrimitives2. |
| [D3DHAL_DP2RESPONSEQUERY structure](ns-d3dhal--d3dhal-dp2responsequery.md) | DirectX 9.0 and later versions only. |
| [D3DHAL_DP2MULTIPLYTRANSFORM structure](ns-d3dhal--d3dhal-dp2multiplytransform.md) | DirectX 8.0 and later versions only. The D3DHAL_DP2MULTIPLYTRANSFORM structure is used to modify the transform matrix for D3dDrawPrimitives2. |
| [D3DHAL_CALLBACKS3 structure](ns-d3dhal--d3dhal-callbacks3~r1.md) | TBD |
| [D3DHAL_DP2TRIANGLEFAN_IMM structure](ns-d3dhal--d3dhal-dp2trianglefan-imm.md) | One D3DHAL_DP2TRIANGLEFAN_IMM structure is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_TRIANGLEFAN_IMM, and is used to render a triangle fan. |
| [D3DHAL_CLEARDATA structure](ns-d3dhal--d3dhal-cleardata.md) | TBD |
| [D3DHAL_DP2SETCLIPPLANE structure](ns-d3dhal--d3dhal-dp2setclipplane.md) | The D3DHAL_SETCLIPPLANE structure allows user defined clip planes to be used in world space. |
| [D3DHAL_DP2CREATEQUERY structure](ns-d3dhal--d3dhal-dp2createquery.md) | DirectX 9.0 and later versions only. |
| [D3DHAL_DP2SETTEXLOD structure](ns-d3dhal--d3dhal-dp2settexlod.md) | The D3DHAL_DP2SETTEXLOD structure is used to set the level of detail (LOD) for MIP maps when the D3DDP2OP_SETTEXLOD command is sent to D3dDrawPrimitives2. |
| [D3DHAL_DP2STARTVERTEX structure](ns-d3dhal--d3dhal-dp2startvertex.md) | A D3DHAL_DP2STARTVERTEX structure follows certain D3DHAL_DP2COMMAND structures in the command buffer, and indicates the offset in the vertex buffer for the first vertex to use in D3dDrawPrimitives2. |
| [D3DHAL_DP2GENERATEMIPSUBLEVELS structure](ns-d3dhal--d3dhal-dp2generatemipsublevels.md) | DirectX 9.0 and later versions only. The D3DHAL_DP2GENERATEMIPSUBLEVELS structure is used to inform the driver to automatically generate the sublevels of a given MIP-map texture using a given filter type. |
| [DDRAWI_DIRECTDRAW_LCL structure](ns-d3dhal--ddrawi-directdraw-lcl.md) | TBD |
| [D3DHAL_CLIPPEDTRIANGLEFAN structure](ns-d3dhal--d3dhal-clippedtrianglefan.md) | DirectX 8.0 and later versions only. |
| [D3DHAL_DP2SETRENDERTARGET structure](ns-d3dhal--d3dhal-dp2setrendertarget.md) | The D3DHAL_DP2SETRENDERTARGET structure is used with the D3DDP2OP_SETRENDERTARGET opcode to map a new rendering target surface and depth buffer in the current context. |
| [D3DLINEPATTERN structure](ns-d3dhal--d3dlinepattern.md) | TBD |
| [D3DHAL_DP2TEXTURESTAGESTATE structure](ns-d3dhal--d3dhal-dp2texturestagestate.md) | One or more D3DHAL_DP2TEXTURESTAGESTATE structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_TEXTURESTAGESTATE, and are used to set the appropriate texture stage state. |
| [D3DHAL_DP2POINTS structure](ns-d3dhal--d3dhal-dp2points.md) | One or more D3DHAL_DP2POINTS structures are parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_POINTS, and are used to render the specified points. |
| [D3DHAL_TEXTUREDESTROYDATA structure](ns-d3dhal--d3dhal-texturedestroydata.md) | TBD |
| [DD_GETDDIVERSIONDATA structure](ns-d3dhal--dd-getddiversiondata.md) | DirectX 9.0 and later versions only. DD_GETDDIVERSIONDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETDDIVERSION. |
| [D3DHAL_DP2INDEXEDTRIANGLEFAN structure](ns-d3dhal--d3dhal-dp2indexedtrianglefan.md) | D3DHAL_DP2INDEXEDTRIANGLEFAN is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDTRIANGLEFAN, and is used to render a sequence of connected triangles using vertex indices. All of the triangles share a common vertex. |
| [D3DHAL_DRAWPRIMCOUNTS structure](ns-d3dhal--d3dhal-drawprimcounts.md) | TBD |
| [D3DHAL_DP2INDEXEDLINELIST structure](ns-d3dhal--d3dhal-dp2indexedlinelist.md) | D3DHAL_DP2INDEXEDLINELIST is parsed from the command buffer by the D3dDrawPrimitives2 callback when the D3DHAL_DP2COMMAND structure's bCommand member is set to D3DDP2OP_INDEXEDLINELIST, and is used to render the lines using vertex indices. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [D3DSI_GETTEXTURETYPE function](nf-d3dhal-d3dsi-gettexturetype.md) | TBD |
| [D3DSI_GETWRITEMASK function](nf-d3dhal-d3dsi-getwritemask.md) | TBD |
| [D3DSI_GETSWIZZLECOMP function](nf-d3dhal-d3dsi-getswizzlecomp.md) | TBD |
| [D3DSI_GETREGISTERPROPERTIES function](nf-d3dhal-d3dsi-getregisterproperties.md) | TBD |
| [D3DVSD_REG function](nf-d3dhal-d3dvsd-reg.md) | TBD |
| [D3DSI_GETREGTYPE_RESOLVING_CONSTANTS function](nf-d3dhal-d3dsi-getregtype-resolving-constants.md) | TBD |
| [D3DSI_GETINSTLENGTH function](nf-d3dhal-d3dsi-getinstlength.md) | TBD |
| [D3DSI_GETSWIZZLE function](nf-d3dhal-d3dsi-getswizzle.md) | TBD |
| [D3DSI_GETREGNUM_RESOLVING_CONSTANTS function](nf-d3dhal-d3dsi-getregnum-resolving-constants.md) | TBD |
| [D3DSI_GETREGTYPE function](nf-d3dhal-d3dsi-getregtype.md) | TBD |
| [D3DVSD_SKIP function](nf-d3dhal-d3dvsd-skip.md) | TBD |
| [D3DVSD_TESSNORMAL function](nf-d3dhal-d3dvsd-tessnormal.md) | TBD |
| [D3DSI_GETCOMPARISON function](nf-d3dhal-d3dsi-getcomparison.md) | TBD |
| [D3DVS_GETSWIZZLE function](nf-d3dhal-d3dvs-getswizzle.md) | TBD |
| [D3DSI_GETREGNUM function](nf-d3dhal-d3dsi-getregnum.md) | TBD |
| [D3DVSD_STREAM function](nf-d3dhal-d3dvsd-stream.md) | TBD |
| [D3DSI_GETOPCODE function](nf-d3dhal-d3dsi-getopcode.md) | TBD |
| [D3DVSD_TESSUV function](nf-d3dhal-d3dvsd-tessuv.md) | TBD |
| [D3DSI_GETUSAGE function](nf-d3dhal-d3dsi-getusage.md) | TBD |
| [D3DSI_GETUSAGEINDEX function](nf-d3dhal-d3dsi-getusageindex.md) | TBD |
| [D3DVS_GETSWIZZLECOMP function](nf-d3dhal-d3dvs-getswizzlecomp.md) | TBD |
| [D3DSI_GETDSTMODIFIER function](nf-d3dhal-d3dsi-getdstmodifier.md) | TBD |
| [D3DSI_GETSRCMODIFIER function](nf-d3dhal-d3dsi-getsrcmodifier.md) | TBD |
| [D3DVSD_MAKETOKENTYPE function](nf-d3dhal-d3dvsd-maketokentype.md) | TBD |
| [D3DSI_GETADDRESSMODE function](nf-d3dhal-d3dsi-getaddressmode.md) | TBD |
| [D3DVSD_CONST function](nf-d3dhal-d3dvsd-const.md) | TBD |
| [D3DVS_GETSRCMODIFIER function](nf-d3dhal-d3dvs-getsrcmodifier.md) | TBD |
| [D3DVS_GETADDRESSMODE function](nf-d3dhal-d3dvs-getaddressmode.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [LPD3DHAL_TEXTUREDESTROYCB callback function](nc-d3dhal-lpd3dhal-texturedestroycb.md) | TBD |
| [LPD3DHAL_TEXTURESWAPCB callback function](nc-d3dhal-lpd3dhal-textureswapcb.md) | TBD |
| [LPD3DHAL_CONTEXTDESTROYCB callback](nc-d3dhal-lpd3dhal-contextdestroycb.md) | The D3dContextDestroy function deletes the specified context. |
| [LPD3DHAL_DRAWPRIMITIVES2CB callback](nc-d3dhal-lpd3dhal-drawprimitives2cb.md) | The D3dDrawPrimitives2 function renders primitives and returns the updated render state. |
| [LPD3DHAL_CONTEXTDESTROYALLCB callback function](nc-d3dhal-lpd3dhal-contextdestroyallcb.md) | TBD |
| [LPD3DHAL_DRAWONEPRIMITIVECB callback function](nc-d3dhal-lpd3dhal-drawoneprimitivecb.md) | TBD |
| [LPD3DHAL_RENDERSTATECB callback function](nc-d3dhal-lpd3dhal-renderstatecb.md) | TBD |
| [LPD3DHAL_DRAWONEINDEXEDPRIMITIVECB callback function](nc-d3dhal-lpd3dhal-drawoneindexedprimitivecb.md) | TBD |
| [LPD3DHAL_DRAWPRIMITIVESCB callback function](nc-d3dhal-lpd3dhal-drawprimitivescb.md) | TBD |
| [LPD3DHAL_CLEARCB callback function](nc-d3dhal-lpd3dhal-clearcb.md) | TBD |
| [LPD3DHAL_SETRENDERTARGETCB callback function](nc-d3dhal-lpd3dhal-setrendertargetcb.md) | TBD |
| [LPD3DHAL_CONTEXTCREATECB callback](nc-d3dhal-lpd3dhal-contextcreatecb.md) | The D3dContextCreate function creates a context. |
| [LPD3DHAL_VALIDATETEXTURESTAGESTATECB callback function](nc-d3dhal-lpd3dhal-validatetexturestagestatecb.md) | TBD |
| [LPD3DHAL_TEXTUREGETSURFCB callback function](nc-d3dhal-lpd3dhal-texturegetsurfcb.md) | TBD |
| [LPD3DHAL_RENDERPRIMITIVECB callback function](nc-d3dhal-lpd3dhal-renderprimitivecb.md) | TBD |
| [LPD3DHAL_TEXTURECREATECB callback function](nc-d3dhal-lpd3dhal-texturecreatecb.md) | TBD |
| [LPD3DHAL_GETSTATECB callback function](nc-d3dhal-lpd3dhal-getstatecb.md) | TBD |
| [LPD3DHAL_SCENECAPTURECB callback function](nc-d3dhal-lpd3dhal-scenecapturecb.md) | TBD |
| [LPD3DHAL_CLEAR2CB callback function](nc-d3dhal-lpd3dhal-clear2cb.md) | TBD |
| [PFND3DPARSEUNKNOWNCOMMAND callback function](nc-d3dhal-pfnd3dparseunknowncommand.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [D3DVSD_TOKENTYPE enumeration](ne-d3dhal--d3dvsd-tokentype.md) | TBD |
| [D3DHAL_DP2OPERATION enumeration](ne-d3dhal--d3dhal-dp2operation.md) | The D3DHAL_DP2OPERATION enumerated type specifies the D3dDrawPrimitives2 operation in the bCommand member of the D3DHAL_DP2COMMAND structure. |

This header is used in these topics:

- [display](..content/_display)
