#!/usr/bin/env python3

formats = [
"PFG_UNKNOWN",
"PFG_RGBA32_FLOAT",
"PFG_RGBA32_UINT",
"PFG_RGBA32_SINT",
"PFG_RGB32_FLOAT",
"PFG_RGB32_UINT",
"PFG_RGB32_SINT",
"PFG_RGBA16_FLOAT",
"PFG_RGBA16_UNORM",
"PFG_RGBA16_UINT",
"PFG_RGBA16_SNORM",
"PFG_RGBA16_SINT",

"PFG_RG32_FLOAT",
"PFG_RG32_UINT",
"PFG_RG32_SINT",

"PFG_D32_FLOAT_S8X24_UINT",

"PFG_R10G10B10A2_UNORM",
"PFG_R10G10B10A2_UINT",
"PFG_R11G11B10_FLOAT",

"PFG_RGBA8_UNORM",
"PFG_RGBA8_UNORM_SRGB",
"PFG_RGBA8_UINT",
"PFG_RGBA8_SNORM",
"PFG_RGBA8_SINT",

"PFG_RG16_FLOAT",
"PFG_RG16_UNORM",
"PFG_RG16_UINT",
"PFG_RG16_SNORM",
"PFG_RG16_SINT",

"PFG_D32_FLOAT",
"PFG_R32_FLOAT",
"PFG_R32_UINT",
"PFG_R32_SINT",

"PFG_D24_UNORM",
"PFG_D24_UNORM_S8_UINT",

"PFG_RG8_UNORM",
"PFG_RG8_UINT",
"PFG_RG8_SNORM",
"PFG_RG8_SINT",

"PFG_R16_FLOAT",
"PFG_D16_UNORM",
"PFG_R16_UNORM",
"PFG_R16_UINT",
"PFG_R16_SNORM",
"PFG_R16_SINT",

"PFG_R8_UNORM",
"PFG_R8_UINT",
"PFG_R8_SNORM",
"PFG_R8_SINT",
"PFG_A8_UNORM",
"PFG_R1_UNORM",
"PFG_R9G9B9E5_SHAREDEXP",




"PFG_R8G8_B8G8_UNORM",

"PFG_G8R8_G8B8_UNORM",


"PFG_BC1_UNORM",
"PFG_BC1_UNORM_SRGB",


"PFG_BC2_UNORM",
"PFG_BC2_UNORM_SRGB",


"PFG_BC3_UNORM",
"PFG_BC3_UNORM_SRGB",


"PFG_BC4_UNORM",

"PFG_BC4_SNORM",

"PFG_BC5_UNORM",
"PFG_BC5_SNORM",

"PFG_B5G6R5_UNORM",
"PFG_B5G5R5A1_UNORM",

"PFG_BGRA8_UNORM",

"PFG_BGRX8_UNORM",
"PFG_R10G10B10_XR_BIAS_A2_UNORM",


"PFG_BGRA8_UNORM_SRGB",

"PFG_BGRX8_UNORM_SRGB",


"PFG_BC6H_UF16",

"PFG_BC6H_SF16",

"PFG_BC7_UNORM",
"PFG_BC7_UNORM_SRGB",

"PFG_AYUV",
"PFG_Y410",
"PFG_Y416",
"PFG_NV12",
"PFG_P010",
"PFG_P016",
"PFG_420_OPAQUE",
"PFG_YUY2",
"PFG_Y210",
"PFG_Y216",
"PFG_NV11",
"PFG_AI44",
"PFG_IA44",
"PFG_P8",
"PFG_A8P8",
"PFG_B4G4R4A4_UNORM",
"PFG_P208",
"PFG_V208",
"PFG_V408",
"PFG_PVRTC_RGB2",

"PFG_PVRTC_RGBA2",

"PFG_PVRTC_RGB4",

"PFG_PVRTC_RGBA4",

"PFG_PVRTC2_2BPP",

"PFG_PVRTC2_4BPP",


"PFG_ETC1_RGB8_UNORM",

"PFG_ETC2_RGB8_UNORM",
"PFG_ETC2_RGB8_UNORM_SRGB",
"PFG_ETC2_RGBA8_UNORM",
"PFG_ETC2_RGBA8_UNORM_SRGB",
"PFG_ETC2_RGB8A1_UNORM",
"PFG_ETC2_RGB8A1_UNORM_SRGB",

"PFG_EAC_R11_UNORM",
"PFG_EAC_R11_SNORM",
"PFG_EAC_R11G11_UNORM",
"PFG_EAC_R11G11_SNORM",

"PFG_ATC_RGB",
"PFG_ATC_RGBA_EXPLICIT_ALPHA",
"PFG_ATC_RGBA_INTERPOLATED_ALPHA"]

for format in formats:
    dxgiFormat = format.replace( "PFG_", "VK_FORMAT_" );
    dxgiFormat = dxgiFormat.replace( "FLOAT", "SFLOAT" );
    dxgiFormat = dxgiFormat.replace( "RGBA8", "R8G8B8A8" )
    dxgiFormat = dxgiFormat.replace( "RGBA16", "R16G16B16A16" )
    dxgiFormat = dxgiFormat.replace( "RGBA32", "R32G32B32A32" )
    dxgiFormat = dxgiFormat.replace( "RGB32", "R32G32B32" )
    dxgiFormat = dxgiFormat.replace( "RG32", "R32G32" )
    dxgiFormat = dxgiFormat.replace( "RG16", "R16G16" )
    dxgiFormat = dxgiFormat.replace( "RG8", "R8G8" )
    final = "case " + format + ":\t\treturn " + dxgiFormat + ";"
    print( final )
