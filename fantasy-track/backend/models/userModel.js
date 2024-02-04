import mongoose from "mongoose";

const userSchema = mongoose.Schema(
    {
        //id generated by mongoose
        
        username: {
            type: String,
            required: true,
        },

        email: {
            type: String,
            required: true,
        },

        password: {
            type: String,
            require: true,
        },

        activeCompetitions: {
            type: [String],
            required: true,
        },
    },

    {
        timestamps : true,
    }
); 
export default userSchema; 
export const User = mongoose.model('User', userSchema); 